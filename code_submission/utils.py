import os
import sys
import filecmp
import re
import subprocess
from subprocess import CalledProcessError, TimeoutExpired


os.environ["PATH"] = os.environ["PATH"]+":/usr/local/cuda/bin/" # adding this line

STATUS_CODES = {
    200: 'OK',
    201: 'ACCEPTED',
    400: 'WRONG ANSWER',
    401: 'COMPILATION ERROR',
    402: 'RUNTIME ERROR',
    403: 'INVALID FILE',
    404: 'FILE NOT FOUND',
    408: 'TIME LIMIT EXCEEDED'
}


class Program:
    """ Class that handles all the methods of a user program """

    def __init__(self, filename, inputfile, timelimit, expectedoutputfile):
        """Receives a name of a file from the userIt must be a valid c, c++, java file """
        self.fileName = filename  # Full name of the source code file
        self.language = None  # Language
        self.name = None  # File name without extension
        self.inputFile = inputfile  # Input file
        self.expectedOutputFile = expectedoutputfile  # Expected output file
        self.actualOutputFile = "./media/compile/output.txt"  # Actual output file
        self.timeLimit = timelimit  # Time limit set for execution in seconds

    def isvalidfile(self):
        """ Checks if the filename is valid """
        validfile = re.compile("^(\S+)\.(java|cpp|c|py)$")
        matches = validfile.match(self.fileName)
        if matches:
            self.name, self.language = matches.groups()
            return True
        return False

    def compile(self):
        """ Compiles the given program, returns status code and errors """

        # Remove previous executables
        if os.path.isfile(self.name):
            os.remove(self.name)

        # Check if files are present
        if not os.path.isfile(self.fileName):
            return 404, 'Missing file'

        # Check language
        cmd = None
        if self.language == 'java':
            cmd = 'javac {}'.format(self.fileName)
        elif self.language == 'py':
            cmd = 'python3 {}'.format(self.fileName)
        elif self.language in ['c', 'cpp']:
            # cmd = 'gcc -o {0} {1}'.format(self.name, self.fileName)
            cmd = 'make {0}'.format(self.name)

        # Invalid files
        if cmd is None:
            return 403, 'File is of invalid type'

        try:
            proc = subprocess.run(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                universal_newlines=True,
                shell=True
            )

            # Check for errors
            if proc.returncode != 0:
                return 401, proc.stderr
            else:
                return 200, None
        except CalledProcessError as e:
            print(e.output)

    def run(self):
        """ Runs the executable, returns status code and errors """

        # Check if files are present
        if not os.path.isfile(self.fileName):
            return 404, 'Missing executable file'

        # Check language
        cmd = None
        if self.language == 'java':
            cmd = 'java {}'.format(self.fileName)
        elif self.language == 'py':
            cmd = 'python3 {}'.format(self.fileName)
        elif self.language in ['c', 'cpp']:
            cmd = './{0}'.format(self.name)

        # Invalid files
        if cmd is None:
            return 403, 'File is of invalid type'

        try:
            with open('./media/compile/output.txt', 'w') as fout:
                fin = None
                if self.inputFile and os.path.isfile(self.inputFile):
                    fin = open(self.inputFile, 'r')
                proc = subprocess.run(
                    cmd,
                    stdin=fin,
                    stdout=fout,
                    stderr=subprocess.PIPE,
                    timeout=self.timeLimit,
                    universal_newlines=True,
                    shell=True
                )

            # Check for errors
            if proc.returncode != 0:
                return 402, proc.stderr
            else:
                return 200, None
        except TimeoutExpired as tle:
            return 408, tle
        except CalledProcessError as e:
            print(e.output)

        # Perform cleanup
        if self.language == 'java':
            os.remove('{}.class'.format(self.name))
        elif self.language in ['c', 'cpp']:
            os.remove(self.name)

    def match(self):
        if os.path.isfile(self.actualOutputFile) and os.path.isfile(self.expectedOutputFile):
            result = filecmp.cmp(self.actualOutputFile, self.expectedOutputFile)
            if result:
                return 201, None
            else:
                return 400, None
        else:
            return 404, 'Missing output files'


def codechecker(filename, inputfile=None, expectedoutput=None, timeout=1, check=True):

    newprogram = Program(
        filename=filename,
        inputfile=inputfile,
        timelimit=timeout,
        expectedoutputfile=expectedoutput
    )
    if newprogram.isvalidfile():
        print('Executing code checker...')
        # Compile program

        compileResult, compileErrors = newprogram.compile()
        print('Compiling... {0}({1})'.format(STATUS_CODES[compileResult], compileResult), flush=True)
        if compileErrors is not None:
            sys.stdout.flush()
            print(compileErrors, file=sys.stderr)
            return STATUS_CODES[compileResult], compileErrors
            exit(0)

        # Run program
        runtimeResult, runtimeErrors = newprogram.run()
        print('Running... {0}({1})'.format(STATUS_CODES[runtimeResult], runtimeResult), flush=True)
        if runtimeErrors is not None:
            sys.stdout.flush()
            print(runtimeErrors, file=sys.stderr)
            return STATUS_CODES[runtimeResult], runtimeErrors
            exit(0)

        if check:
            # Match expected output
            matchResult, matchErrors = newprogram.match()
            print('Verdict... {0}({1})'.format(STATUS_CODES[matchResult], matchResult), flush=True)
            if matchErrors is not None:
                sys.stdout.flush()
                print(matchErrors, file=sys.stderr)
                return STATUS_CODES[matchResult], matchErrors
                exit(0)
            else:
                return STATUS_CODES[matchResult], 'Accepted'
    else:
        print('FATAL: Invalid file', file=sys.stderr)
        return 403, 'Invalid file'


# if __name__ == '__main__':
#
#     # cmd = 'python3 test.py'
#     #
#     # try:
#     #     rs = subprocess.run(
#     #         cmd,
#     #         stdout=subprocess.PIPE,
#     #         stderr=subprocess.PIPE,
#     #         universal_newlines=True,
#     #         shell=True
#     #     )
#     #
#     #     if rs.returncode != 0:
#     #         print(401, rs.stderr)
#     #     else:
#     #         print("Run oce")
#     # except CalledProcessError as e:
#     #     print(e.output)
#
#     codechecker(
#         filename='test.py',               # Source code file
#         inputfile='input.txt',                  # Input file
#         expectedoutput='correctoutput.txt',     # Expected output
#         timeout=1,                              # Time limit
#         check=True                              # Set to true to check actual output against expected output
#     )


def check_main(path_to_source, input_file, output_file, time_limit):
    code_result, notes_result = codechecker(
        filename=path_to_source,  # Source code file
        inputfile=input_file,  # Input file
        expectedoutput=output_file,  # Expected output
        timeout=time_limit,  # Time limit
        check=True
    )

    return code_result, notes_result


""" Command to compile """
# Java: javac <path to file>
# Python: python3 <path to file>
# C: clang <path to file> -o <name file>
# C++: make <file>

""" Run to complie """
# Java: java <path to file>
# Python: python3 <path to file>
# C: <path to file>
# C++: <path to file>
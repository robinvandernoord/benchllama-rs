import pandas as pd
from pathlib import Path

from ..constants import Result
from .runners.python_runner import PythonRunner

from .runners.cpp_runner import CppRunner
from .runners.rust_runner import RustRunner
from .runners.java_runner import JavaRunner
from .runners.javascript_runner import JavascriptRunner
from .runners.go_runner import GoRunner


class CodeRunner:
    def __init__(self, execution_dir: Path):
        self.execution_dir = execution_dir

        self.runners = {
            "cpp": CppRunner(execution_dir),
            "go": GoRunner(execution_dir),
            "javacript": JavascriptRunner(execution_dir),
            "java": JavaRunner(execution_dir),
            "python": PythonRunner(execution_dir),
            "rust": RustRunner(execution_dir),
        }

    def run(self, problem: pd.Series):
        language = problem["language"].lower()

        if language not in self.runners:
            return Result.FAILURE, "Language not supported!"

        return self.runners[language].run(problem)

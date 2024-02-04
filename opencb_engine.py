
print("""
   ____                    _____ ____  
  / __ \                  / ____|  _ \ 
 | |  | |_ __   ___ _ __ | |    | |_) |
 | |  | | '_ \ / _ \ '_ \| |    |  _ < 
 | |__| | |_) |  __/ | | | |____| |_) |
  \____/| .__/ \___|_| |_|\_____|____/ 
        | |                            
        |_|                             
        """)
     
import ast
from tqdm import tqdm
import time

class OpenCBEngine:
    def __init__(self, engine_type):
        self.engine_type = engine_type
        self.supported_engine_types = ["opencv-1", "opencv-2", "opencv-3", "opencv4-5turbo"]

    def analyze_code(self, code_path):
        if self.engine_type not in self.supported_engine_types:
            return f"Error: Engine type '{self.engine_type}' is not supported."

        if self.engine_type == "opencv-1":
            return self.basic_code_analysis(code_path)
        elif self.engine_type == "opencv-2":
            return self.basic_and_complexity_analysis(code_path)
        elif self.engine_type == "opencv-3":
            return self.basic_complexity_bug_detection_analysis(code_path)
        elif self.engine_type == "opencv4-5turbo":
            return self.all_detections_analysis(code_path)
        else:
            return "Error: Invalid engine type."

    def basic_code_analysis(self, code_path):
        try:
            with open(code_path, 'r') as file:
                source_code = file.read()

            tree = ast.parse(source_code)

            function_count = sum(1 for node in tqdm(ast.walk(tree), desc="Analyzing functions", unit=" functions") if isinstance(node, ast.FunctionDef))
            class_count = sum(1 for node in tqdm(ast.walk(tree), desc="Analyzing classes", unit=" classes") if isinstance(node, ast.ClassDef))

            self.process_with_progress_bar(1, "Basic code analysis")
            
            report = f"\nBasic code analysis for {code_path}:\n"
            report += f"Number of functions: {function_count}\n"
            report += f"Number of classes: {class_count}\n"

            return report

        except FileNotFoundError:
            return f"Basic code analysis failed. File not found: {code_path}"
        except Exception as e:
            return f"Basic code analysis failed. Error: {str(e)}"

    def basic_and_complexity_analysis(self, code_path):
        report = self.basic_code_analysis(code_path)
        report += self.complexity_analysis(code_path)
        return report

    def basic_complexity_bug_detection_analysis(self, code_path):
        report = self.basic_and_complexity_analysis(code_path)
        report += self.bug_detection(code_path)
        return report

    def all_detections_analysis(self, code_path):
        report = self.basic_complexity_bug_detection_analysis(code_path)
        report += self.predictive_analysis(code_path)
        return report

    def complexity_analysis(self, code_path):
        try:
            with open(code_path, 'r') as file:
                source_code = file.read()

            tree = ast.parse(source_code)
            complexity = self.calculate_complexity(tree)

            self.process_with_progress_bar(1, "Complexity analysis")

            report = f"\nComplexity analysis for {code_path}:\n"
            report += f"Custom complexity metric: {complexity}\n"

            return report

        except FileNotFoundError:
            return f"Complexity analysis failed. File not found: {code_path}"
        except Exception as e:
            return f"Complexity analysis failed. Error: {str(e)}"

    def calculate_complexity(self, node):
        complexity = 0

        for item in tqdm(ast.walk(node), desc="Calculating complexity", unit=" nodes"):
            if isinstance(item, ast.If) or isinstance(item, ast.While) or isinstance(item, ast.For):
                complexity += 1

        return complexity

    def bug_detection(self, code_path):
        try:
            with open(code_path, 'r') as file:
                source_code = file.read()

            tree = ast.parse(source_code)

            transformer = BugDetectionTransformer()
            transformed_tree = transformer.visit(tree)

            errors_found = transformer.get_errors()

            self.process_with_progress_bar(1, "Bug detection analysis")

            report = f"\nBug detection analysis for {code_path}:\n"
            report += f"{len(errors_found)} errors found.\n"
            for error in tqdm(errors_found, desc="Detecting bugs", unit=" errors"):
                report += f"- {error}\n"

            return report

        except FileNotFoundError:
            return f"Bug detection analysis failed. File not found: {code_path}"
        except Exception as e:
            return f"Bug detection analysis failed. Error: {str(e)}"

    def predictive_analysis(self, code_path):
        try:
            with open(code_path, 'r') as file:
                source_code = file.read()

            tree = ast.parse(source_code)
            visitor = PredictiveAnalysisVisitor()
            visitor.visit(tree)

            unused_variables = visitor.get_unused_variables()

            self.process_with_progress_bar(10, "Predictive analysis")

            report = f"\nPredictive analysis for {code_path}:\n"
            if unused_variables:
                report += f"Potential issues detected:\n"
                for variable in tqdm(unused_variables, desc="Analyzing potential issues", unit=" variables"):
                    report += f"- Unused variable: {variable}\n"
            else:
                report += "No potential issues detected."

            return report

        except FileNotFoundError:
            return f"Predictive analysis failed. File not found: {code_path}"
        except Exception as e:
            return f"Predictive analysis failed. Error: {str(e)}"

    def process_with_progress_bar(self, duration, process_name):
        with tqdm(total=duration, desc=f"{process_name} Processing", unit=" seconds") as pbar:
            for _ in range(duration):
                time.sleep(1)
                pbar.update(1)


class BugDetectionTransformer(ast.NodeTransformer):
    def __init__(self):
        self.errors_found = []

    def get_errors(self):
        return self.errors_found

    def visit_Str(self, node):
        if not node.s.isalnum():
            self.errors_found.append(f"Non-alphanumeric string detected in line {node.lineno}: {node.s}")

        return self.generic_visit(node)

    def visit_Expr(self, node):
        if isinstance(node.value, ast.Str) or isinstance(node.value, ast.Expr):
            if not node.value.s.endswith(';'):
                self.errors_found.append(f"Missing semicolon at the end of statement in line {node.lineno}")

        return self.generic_visit(node)

    def visit_Name(self, node):
        if not node.id.isalnum():
            self.errors_found.append(f"Wrong symbol detected in variable name '{node.id}' in line {node.lineno}")

        return self.generic_visit(node)


class PredictiveAnalysisVisitor(ast.NodeVisitor):
    def __init__(self):
        self.variables_defined = set()
        self.variables_used = set()

    def visit_FunctionDef(self, node):
        self.variables_defined.add(node.name)
        self.generic_visit(node)

    def visit_Assign(self, node):
        for target in node.targets:
            if isinstance(target, ast.Name):
                self.variables_defined.add(target.id)
        self.generic_visit(node)

    def visit_Name(self, node):
        if isinstance(node.ctx, ast.Load):
            self.variables_used.add(node.id)
        self.generic_visit(node)

    def get_unused_variables(self):
        return self.variables_defined - self.variables_used


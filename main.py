# tester.py

from opencb_engine import OpenCBEngine

# Example usage
engine_type = "opencv4-5turbo"
code_path = "/storage/emulated/0/OpenCB (Bug Detector)filename.py"

opencb_engine = OpenCBEngine(engine_type)
result = opencb_engine.analyze_code(code_path)

print(result)
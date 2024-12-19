from roboflow import Roboflow
rf = Roboflow(api_key="xxbcTrSTvfSiwWkHHCUE")
project = rf.workspace("andrei-dore-5lz05").project("acne04")
version = project.version(1)
dataset = version.download("yolov11")
                
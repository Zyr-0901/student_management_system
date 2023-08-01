import os
import yaml


class DealYaml:
    @staticmethod
    def load_yaml(path):
        project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        real_path = os.path.join(project_dir, path)
        with open(real_path, encoding="utf-8") as f:
            result = yaml.safe_load(f)
            return result

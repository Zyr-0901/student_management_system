import os
import yaml


class OperateYaml:
    @staticmethod
    def read_yaml(path):
        cur_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        target_path = os.path.join(cur_dir, path)
        with open(target_path, encoding='utf-8') as f:
            results = yaml.safe_load(f)
            return results


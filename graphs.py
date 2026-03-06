import pandas as pd
import numpy as np

class Graph:
    def data(self, train_file):
        self.file_data = train_file
        
        # 1. Find all literal hyphens and replace them with mathematical NaNs
        self.file_data = self.file_data.replace('-', 0)
        
        self.file_data = self.file_data.dropna()
        
        return self.file_data
import matplotlib.pyplot as plt
import pandas as pd
from predict import light
class Graph:
    def data(self, trian_file):
        self.file_data = trian_file
        self.file_data=self.file_data.dropna()
        return self.file_data
    
        
        



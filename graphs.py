import matplotlib.pyplot as plt
import pandas as pd


class Graph:
    def data(self, trian_file):
        self.file_data = trian_file
        self.file_data=self.file_data.dropna()
        return self.file_data

    def predict(self):
        data=self.file_data
        
        



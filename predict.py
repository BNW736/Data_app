import pandas as pd
import lightgbm as lb


class light():
    def clasifer(self,data):
        self.clean=data
        
    def lightgbm(self,x,y):
        
        self.x_clean=self.clean[x].astype(str).str.replace(',', '').astype(float)
        self.y_clean=self.clean[y]
        model = lb.LGBMClassifier(
            boosting_type="gbdt",
            n_jobs=-1,
            learning_rate=0.0003,
            random_state=41,
            n_estimators=100,
            verbose=-1
        )
        model.fit(self.x_clean,self.y_clean)
        predict = model.predict(self.x_clean)
        return predict

import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    self_view = views[views["author_id"] == views["viewer_id"]]
    self_view = self_view.sort_values("author_id", ascending  = True)
    self_view = self_view[["author_id"]] 
    self_view.columns = ["id"]
    self_view = self_view.drop_duplicates()
    return self_view

    
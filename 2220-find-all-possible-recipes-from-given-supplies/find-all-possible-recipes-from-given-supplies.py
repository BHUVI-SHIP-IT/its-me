class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        created_rec=[]
        rec_ing=dict(zip(recipes,ingredients))
        available=set(supplies)
        created=True
        while created:
            created=False
            for rec,ings in list(rec_ing.items()):
                if  all(ing in available for ing in ings):
                    created_rec.append(rec)
                    available.add(rec)
                    del rec_ing[rec]
                    created = True
        return created_rec
            
        
        
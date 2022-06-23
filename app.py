from flask import Flask,render_template, request
import pickle
import numpy as np

pop_df = pickle.load(open('popular.pkl','rb'))
pt = pickle.load(open('pt.pkl','rb'))
book = pickle.load(open('book.pkl','rb'))
ss = pickle.load(open('ss.pkl','rb'))
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',
                            book_name = list(pop_df['Book-Title'].values),
                            author = list(pop_df['Book-Author'].values),
                            image = list(pop_df['Image-URL-L'].values),
                            reads = list(pop_df['Num_of_Votes'].values),
                            rating = list(pop_df['Average_Rating'].values)
                            )

@app.route('/recommend.html')
def rec():
    return render_template('recommend.html')

@app.route('/recommend_books' ,methods=['POST'])
def recommend():
    user_input = request.form.get('user_input')
    index = np.where(pt.index == user_input)[0][0]
    similar_item = sorted(list(enumerate(ss[index])), key = lambda x:x[1], reverse =True)[1:6]
    
    data=[]
    for i in similar_item:
        item = []
        temp = book[book['Book-Title'] == pt.index[i[0]]]
        item.extend(list(temp.drop_duplicates('Book-Title')['Book-Title'].values))
        item.extend(list(temp.drop_duplicates('Book-Title')['Book-Author'].values))
        item.extend(list(temp.drop_duplicates('Book-Title')['Image-URL-L'].values))
        data.append(item)
    return render_template('recommend.html', data = data)
  

if __name__ == '__main__':
    app.run(debug = True)

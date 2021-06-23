from flask import Flask,request,jsonify
from storage import all_articles , liked_articles , not_likes_articles , did_not_read_articles
from demographic_filtering import output
from content_filtering import getRecommendation

app = Flask(__name__)

@app.route('/get-article')
def get_Article():
    article_Data = {
        'title':all_articles[0][12],
        'url':all_articles[0][11],
        'lang':all_articles[0][14] or 'n/a',
        'contentId':all_articles[0][4],
        'authorPersonId':all_articles[0][5],
        'total_events':all_articles[0][15]
    }
    return jsonify({
        'data':article_Data,
        'status':'success'
    })

@app.route('/liked-article',methods = ['POST'])
def liked_article():
    article = all_articles[0]
    liked_articles.append(article)
    all_articles.pop(0)
    return jsonify({
        'status':'success'
    }),201

@app.route('/unliked-article',methods = ['POST'])
def unliked_article():
    article = all_articles[0]
    not_likes_articles.append(article)
    all_articles.pop(0)
    return jsonify({
        'status':'success'
    }),201

@app.route('/did_not_read-article',methods = ['POST'])
def did_not_read_article():
    article = all_articles[0]
    did_not_read_articles.append(article)
    all_articles.pop(0)
    return jsonify({
        'status':'success'
    }),201

@app.route('/popular-articles')
def popular_articles():
    article_data = []
    for i in output:
        data = {
            'title':i[0],
            'url':i[1],
            'lang':i[2] or 'n/a',
            'contentId':i[3],
            'authorPersonId':i[4],
            'total_events':i[5]
        }
        article_data.append(data)

    return jsonify({
        'data':article_data,
        'status':'success'
    }),201

@app.route('/recommeded-articles')
def recommended_articles():
    all_recommended = []
    for i in liked_articles:
        output = getRecommendation(i[19])
        for data in output:
            all_recommended.append(data)
    
    import itertools
    all_recommended.sort()

    all_recommended = list(all_recommended for all_recommended,_ in itertools.groupby(all_recommended))

    article_data = []
    for i in all_recommended:
        data = {
            'title':i[0],
            'url':i[1],
            'lang':i[2] or 'n/a',
            'contentId':i[3],
            'authorPersonId':i[4],
            'total_events':i[5]
        }
        article_data.append(data)
    
    return jsonify({
        'data':article_data,
        'status':'success'
    }),201

if __name__ == '__main__':
    app.run()
# from transformers import BertTokenizer, BertForSequenceClassification
#
# tokenizer = BertTokenizer.from_pretrained('bert-base-chinese')
# model = BertForSequenceClassification.from_pretrained('bert-base-chinese', num_labels=2).to('cuda')
#
# # 保存模型和分词器
# model.save_pretrained('./sentiment_model')
# tokenizer.save_pretrained('./sentiment_model')

from transformers import pipeline

# 加载训练好的模型和分词器
classifier = pipeline('sentiment-analysis', model='./sentiment_model', tokenizer='./sentiment_model')

# 进行情感预测
result = classifier("我感觉到很无助")
print(result)

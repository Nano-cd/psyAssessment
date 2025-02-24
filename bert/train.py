import mlflow
from transformers import BertTokenizer, BertForSequenceClassification
mlflow.set_experiment("Bert Model")
# 加载 BERT 中文预训练模型和分词器
tokenizer = BertTokenizer.from_pretrained('bert-base-chinese')
model = BertForSequenceClassification.from_pretrained('bert-base-chinese', num_labels=2).to('cuda')

from datasets import load_dataset

# 加载 ChnSentiCorp 数据集
dataset = load_dataset('lansinuote/ChnSentiCorp')


def tokenize_function(examples):
    return tokenizer(examples['text'], padding='max_length', truncation=True)


# 对数据集进行分词和编码
encoded_dataset = dataset.map(tokenize_function, batched=True)

from transformers import Trainer, TrainingArguments

training_args = TrainingArguments(
    output_dir='./results',
    num_train_epochs=10,
    per_device_train_batch_size=16,
    per_device_eval_batch_size=16,
    evaluation_strategy="epoch",
    logging_dir='./logs',
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=encoded_dataset['train'],
    eval_dataset=encoded_dataset['validation'],

)

# 开始训练
trainer.train()
# 保存模型和分词器
model.save_pretrained('./sentiment_model')
tokenizer.save_pretrained('./sentiment_model')

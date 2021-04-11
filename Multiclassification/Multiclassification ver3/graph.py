import matplotlib.pyplot as plt

# show in two graph
def show_graph(history_dict):
    accuracy = history_dict['accuracy']
    loss = history_dict['loss']

    epochs = range(1, len(loss) + 1)
    
    plt.figure(figsize=(12, 5))
    plt.subplot(1,2,1) # 위치 지정
    plt.plot(epochs, accuracy, 'ro', label='Training accuracy')
    plt.title('Trainging and validation accuracy and loss')
    plt.xlabel('Epochs')
    plt.ylabel('Accuracy and Loss')
    plt.legend(bbox_to_anchor=(1, -0.1))

    plt.subplot(1,2,2)
    plt.plot(epochs, loss, 'bo', label='Training loss')
    plt.title('Training and validation loss')
    plt.xlabel('Epochs')
    plt.ylabel('Loss')
    
    plt.legend(bbox_to_anchor=(1, -0.1))
    plt.show()


class CorpusHandler:

    def save_corpus(list_sentences,output_filename):

        with open(f"training_data/{output_filename}.txt","w",encoding='utf-8') as file:
            
            for sentence in list_sentences:
                file.write(sentence+"\n")
    
    
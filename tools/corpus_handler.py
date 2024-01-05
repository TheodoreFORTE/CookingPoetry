

class CorpusHandler:

    def save_corpus(list_sentences,output_filename):

        with open(f"corpus/{output_filename}.txt","w",encoding='utf-8') as file:
            
            for sentence in list_sentences:
                file.write(sentence+"\n")
    
    def load_corpus(filename):

        with open(f"corpus/{filename}.txt","r") as file: 
            lines = [line.strip() for line in file.readlines()]
            return lines

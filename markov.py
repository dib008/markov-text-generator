import random

def build_markov_chain(text):
    words = text.split()
    markov_chain = {}
    for i in range(len(words) - 1):
        curr_word = words[i]
        next_word = words[i + 1]
        if curr_word in markov_chain:
            markov_chain[curr_word].append(next_word)
        else:
            markov_chain[curr_word] = [next_word]
    return markov_chain

def generate_text(chain, length=20):
    curr_word = random.choice(list(chain.keys()))
    output = [curr_word]
    for _ in range(length - 1):
        next_words = chain.get(curr_word, None)
        if not next_words:
            curr_word = random.choice(list(chain.keys()))
        else:
            curr_word = random.choice(next_words)
        output.append(curr_word)
    return ' '.join(output)

if __name__ == "__main__":
    # Read sample input
    with open('example.txt', 'r') as f:
        data = f.read()
    chain = build_markov_chain(data)
    generated = generate_text(chain, 50)
    print(generated)
    # Save output
    with open('output.txt', 'w') as out:
        out.write(generated)
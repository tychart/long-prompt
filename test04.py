import requests
import re
from pprint import pprint
import argparse

# Ollama API endpoint
api_endpoint = 'http://192.168.10.35:11434/api/chat'
api_endpoint_k8s = 'http://10.11.14.221:11434/api/chat'




zprompt = "Can you please give me a sentence by sentance sparknotes of the following in modern language with relatively easy vocabulary? These are completely in the public domain so don't worry about copyright."

ztext = """Book I 	   Go to next

Part 1



"ALL men by nature desire to know. An indication of this is the delight we take in our senses; for even apart from their usefulness they are loved for themselves; and above all others the sense of sight. For not only with a view to action, but even when we are not going to do anything, we prefer seeing (one might say) to everything else. The reason is that this, most of all the senses, makes us know and brings to light many differences between things.

"By nature animals are born with the faculty of sensation, and from sensation memory is produced in some of them, though not in others. And therefore the former are more intelligent and apt at learning than those which cannot remember; those which are incapable of hearing sounds are intelligent though they cannot be taught, e.g. the bee, and any other race of animals that may be like it; and those which besides memory have this sense of hearing can be taught.

"The animals other than man live by appearances and memories, and have but little of connected experience; but the human race lives also by art and reasonings. Now from memory experience is produced in men; for the several memories of the same thing produce finally the capacity for a single experience. And experience seems pretty much like science and art, but really science and art come to men through experience; for 'experience made art', as Polus says, 'but inexperience luck.' Now art arises when from many notions gained by experience one universal judgement about a class of objects is produced. For to have a judgement that when Callias was ill of this disease this did him good, and similarly in the case of Socrates and in many individual cases, is a matter of experience; but to judge that it has done good to all persons of a certain constitution, marked off in one class, when they were ill of this disease, e.g. to phlegmatic or bilious people when burning with fevers-this is a matter of art.

"With a view to action experience seems in no respect inferior to art, and men of experience succeed even better than those who have theory without experience. (The reason is that experience is knowledge of individuals, art of universals, and actions and productions are all concerned with the individual; for the physician does not cure man, except in an incidental way, but Callias or Socrates or some other called by some such individual name, who happens to be a man. If, then, a man has the theory without the experience, and recognizes the universal but does not know the individual included in this, he will often fail to cure; for it is the individual that is to be cured.) But yet we think that knowledge and understanding belong to art rather than to experience, and we suppose artists to be wiser than men of experience (which implies that Wisdom depends in all cases rather on knowledge); and this because the former know the cause, but the latter do not. For men of experience know that the thing is so, but do not know why, while the others know the 'why' and the cause. Hence we think also that the masterworkers in each craft are more honourable and know in a truer sense and are wiser than the manual workers, because they know the causes of the things that are done (we think the manual workers are like certain lifeless things which act indeed, but act without knowing what they do, as fire burns,-but while the lifeless things perform each of their functions by a natural tendency, the labourers perform them through habit); thus we view them as being wiser not in virtue of being able to act, but of having the theory for themselves and knowing the causes. And in general it is a sign of the man who knows and of the man who does not know, that the former can teach, and therefore we think art more truly knowledge than experience is; for artists can teach, and men of mere experience cannot.

"Again, we do not regard any of the senses as Wisdom; yet surely these give the most authoritative knowledge of particulars. But they do not tell us the 'why' of anything-e.g. why fire is hot; they only say that it is hot.

"At first he who invented any art whatever that went beyond the common perceptions of man was naturally admired by men, not only because there was something useful in the inventions, but because he was thought wise and superior to the rest. But as more arts were invented, and some were directed to the necessities of life, others to recreation, the inventors of the latter were naturally always regarded as wiser than the inventors of the former, because their branches of knowledge did not aim at utility. Hence when all such inventions were already established, the sciences which do not aim at giving pleasure or at the necessities of life were discovered, and first in the places where men first began to have leisure. This is why the mathematical arts were founded in Egypt; for there the priestly caste was allowed to be at leisure.

"We have said in the Ethics what the difference is between art and science and the other kindred faculties; but the point of our present discussion is this, that all men suppose what is called Wisdom to deal with the first causes and the principles of things; so that, as has been said before, the man of experience is thought to be wiser than the possessors of any sense-perception whatever, the artist wiser than the men of experience, the masterworker than the mechanic, and the theoretical kinds of knowledge to be more of the nature of Wisdom than the productive. Clearly then Wisdom is knowledge about certain principles and causes.

Part 2 "



"Since we are seeking this knowledge, we must inquire of what kind are the causes and the principles, the knowledge of which is Wisdom. If one were to take the notions we have about the wise man, this might perhaps make the answer more evident. We suppose first, then, that the wise man knows all things, as far as possible, although he has not knowledge of each of them in detail; secondly, that he who can learn things that are difficult, and not easy for man to know, is wise (sense-perception is common to all, and therefore easy and no mark of Wisdom); again, that he who is more exact and more capable of teaching the causes is wiser, in every branch of knowledge; and that of the sciences, also, that which is desirable on its own account and for the sake of knowing it is more of the nature of Wisdom than that which is desirable on account of its results, and the superior science is more of the nature of Wisdom than the ancillary; for the wise man must not be ordered but must order, and he must not obey another, but the less wise must obey him.

"Such and so many are the notions, then, which we have about Wisdom and the wise. Now of these characteristics that of knowing all things must belong to him who has in the highest degree universal knowledge; for he knows in a sense all the instances that fall under the universal. And these things, the most universal, are on the whole the hardest for men to know; for they are farthest from the senses. And the most exact of the sciences are those which deal most with first principles; for those which involve fewer principles are more exact than those which involve additional principles, e.g. arithmetic than geometry. But the science which investigates causes is also instructive, in a higher degree, for the people who instruct us are those who tell the causes of each thing. And understanding and knowledge pursued for their own sake are found most in the knowledge of that which is most knowable (for he who chooses to know for the sake of knowing will choose most readily that which is most truly knowledge, and such is the knowledge of that which is most knowable); and the first principles and the causes are most knowable; for by reason of these, and from these, all other things come to be known, and not these by means of the things subordinate to them. And the science which knows to what end each thing must be done is the most authoritative of the sciences, and more authoritative than any ancillary science; and this end is the good of that thing, and in general the supreme good in the whole of nature. Judged by all the tests we have mentioned, then, the name in question falls to the same science; this must be a science that investigates the first principles and causes; for the good, i.e. the end, is one of the causes.

"That it is not a science of production is clear even from the history of the earliest philosophers. For it is owing to their wonder that men both now begin and at first began to philosophize; they wondered originally at the obvious difficulties, then advanced little by little and stated difficulties about the greater matters, e.g. about the phenomena of the moon and those of the sun and of the stars, and about the genesis of the universe. And a man who is puzzled and wonders thinks himself ignorant (whence even the lover of myth is in a sense a lover of Wisdom, for the myth is composed of wonders); therefore since they philosophized order to escape from ignorance, evidently they were pursuing science in order to know, and not for any utilitarian end. And this is confirmed by the facts; for it was when almost all the necessities of life and the things that make for comfort and recreation had been secured, that such knowledge began to be sought. Evidently then we do not seek it for the sake of any other advantage; but as the man is free, we say, who exists for his own sake and not for another's, so we pursue this as the only free science, for it alone exists for its own sake.

"Hence also the possession of it might be justly regarded as beyond human power; for in many ways human nature is in bondage, so that according to Simonides 'God alone can have this privilege', and it is unfitting that man should not be content to seek the knowledge that is suited to him. If, then, there is something in what the poets say, and jealousy is natural to the divine power, it would probably occur in this case above all, and all who excelled in this knowledge would be unfortunate. But the divine power cannot be jealous (nay, according to the proverb, 'bards tell a lie'), nor should any other science be thought more honourable than one of this sort. For the most divine science is also most honourable; and this science alone must be, in two ways, most divine. For the science which it would be most meet for God to have is a divine science, and so is any science that deals with divine objects; and this science alone has both these qualities; for (1) God is thought to be among the causes of all things and to be a first principle, and (2) such a science either God alone can have, or God above all others. All the sciences, indeed, are more necessary than this, but none is better.

"Yet the acquisition of it must in a sense end in something which is the opposite of our original inquiries. For all men begin, as we said, by wondering that things are as they are, as they do about self-moving marionettes, or about the solstices or the incommensurability of the diagonal of a square with the side; for it seems wonderful to all who have not yet seen the reason, that there is a thing which cannot be measured even by the smallest unit. But we must end in the contrary and, according to the proverb, the better state, as is the case in these instances too when men learn the cause; for there is nothing which would surprise a geometer so much as if the diagonal turned out to be commensurable.

"We have stated, then, what is the nature of the science we are searching for, and what is the mark which our search and our whole investigation must reach.

Part 3 "



"Evidently we have to acquire knowledge of the original causes (for we say we know each thing only when we think we recognize its first cause), and causes are spoken of in four senses. In one of these we mean the substance, i.e. the essence (for the 'why' is reducible finally to the definition, and the ultimate 'why' is a cause and principle); in another the matter or substratum, in a third the source of the change, and in a fourth the cause opposed to this, the purpose and the good (for this is the end of all generation and change). We have studied these causes sufficiently in our work on nature, but yet let us call to our aid those who have attacked the investigation of being and philosophized about reality before us. For obviously they too speak of certain principles and causes; to go over their views, then, will be of profit to the present inquiry, for we shall either find another kind of cause, or be more convinced of the correctness of those which we now maintain.

"Of the first philosophers, then, most thought the principles which were of the nature of matter were the only principles of all things. That of which all things that are consist, the first from which they come to be, the last into which they are resolved (the substance remaining, but changing in its modifications), this they say is the element and this the principle of things, and therefore they think nothing is either generated or destroyed, since this sort of entity is always conserved, as we say Socrates neither comes to be absolutely when he comes to be beautiful or musical, nor ceases to be when loses these characteristics, because the substratum, Socrates himself remains. just so they say nothing else comes to be or ceases to be; for there must be some entity-either one or more than one-from which all other things come to be, it being conserved.

"Yet they do not all agree as to the number and the nature of these principles. Thales, the founder of this type of philosophy, says the principle is water (for which reason he declared that the earth rests on water), getting the notion perhaps from seeing that the nutriment of all things is moist, and that heat itself is generated from the moist and kept alive by it (and that from which they come to be is a principle of all things). He got his notion from this fact, and from the fact that the seeds of all things have a moist nature, and that water is the origin of the nature of moist things.

"Some think that even the ancients who lived long before the present generation, and first framed accounts of the gods, had a similar view of nature; for they made Ocean and Tethys the parents of creation, and described the oath of the gods as being by water, to which they give the name of Styx; for what is oldest is most honourable, and the most honourable thing is that by which one swears. It may perhaps be uncertain whether this opinion about nature is primitive and ancient, but Thales at any rate is said to have declared himself thus about the first cause. Hippo no one would think fit to include among these thinkers, because of the paltriness of his thought.

"Anaximenes and Diogenes make air prior to water, and the most primary of the simple bodies, while Hippasus of Metapontium and Heraclitus of Ephesus say this of fire, and Empedocles says it of the four elements (adding a fourth-earth-to those which have been named); for these, he says, always remain and do not come to be, except that they come to be more or fewer, being aggregated into one and segregated out of one.

"Anaxagoras of Clazomenae, who, though older than Empedocles, was later in his philosophical activity, says the principles are infinite in number; for he says almost all the things that are made of parts like themselves, in the manner of water or fire, are generated and destroyed in this way, only by aggregation and segregation, and are not in any other sense generated or destroyed, but remain eternally.

"From these facts one might think that the only cause is the so-called material cause; but as men thus advanced, the very facts opened the way for them and joined in forcing them to investigate the subject. However true it may be that all generation and destruction proceed from some one or (for that matter) from more elements, why does this happen and what is the cause? For at least the substratum itself does not make itself change; e.g. neither the wood nor the bronze causes the change of either of them, nor does the wood manufacture a bed and the bronze a statue, but something else is the cause of the change. And to seek this is to seek the second cause, as we should say,-that from which comes the beginning of the movement. Now those who at the very beginning set themselves to this kind of inquiry, and said the substratum was one, were not at all dissatisfied with themselves; but some at least of those who maintain it to be one-as though defeated by this search for the second cause-say the one and nature as a whole is unchangeable not only in respect of generation and destruction (for this is a primitive belief, and all agreed in it), but also of all other change; and this view is peculiar to them. Of those who said the universe was one, then none succeeded in discovering a cause of this sort, except perhaps Parmenides, and he only inasmuch as he supposes that there is not only one but also in some sense two causes. But for those who make more elements it is more possible to state the second cause, e.g. for those who make hot and cold, or fire and earth, the elements; for they treat fire as having a nature which fits it to move things, and water and earth and such things they treat in the contrary way.

"When these men and the principles of this kind had had their day, as the latter were found inadequate to generate the nature of things men were again forced by the truth itself, as we said, to inquire into the next kind of cause. For it is not likely either that fire or earth or any such element should be the reason why things manifest goodness and, beauty both in their being and in their coming to be, or that those thinkers should have supposed it was; nor again could it be right to entrust so great a matter to spontaneity and chance. When one man said, then, that reason was present-as in animals, so throughout nature-as the cause of order and of all arrangement, he seemed like a sober man in contrast with the random talk of his predecessors. We know that Anaxagoras certainly adopted these views, but Hermotimus of Clazomenae is credited with expressing them earlier. Those who thought thus stated that there is a principle of things which is at the same time the cause of beauty, and that sort of cause from which things acquire movement.

Part 4 "



"One might suspect that Hesiod was the first to look for such a thing-or some one else who put love or desire among existing things as a principle, as Parmenides, too, does; for he, in constructing the genesis of the universe, says:- "



"Love first of all the Gods she planned. "



"And Hesiod says:- "



"First of all things was chaos made, and then

"Broad-breasted earth...

"And love, 'mid all the gods pre-eminent, "



which implies that among existing things there must be from the first a cause which will move things and bring them together. How these thinkers should be arranged with regard to priority of discovery let us be allowed to decide later; but since the contraries of the various forms of good were also perceived to be present in nature-not only order and the beautiful, but also disorder and the ugly, and bad things in greater number than good, and ignoble things than beautiful-therefore another thinker introduced friendship and strife, each of the two the cause of one of these two sets of qualities. For if we were to follow out the view of Empedocles, and interpret it according to its meaning and not to its lisping expression, we should find that friendship is the cause of good things, and strife of bad. Therefore, if we said that Empedocles in a sense both mentions, and is the first to mention, the bad and the good as principles, we should perhaps be right, since the cause of all goods is the good itself.

"These thinkers, as we say, evidently grasped, and to this extent, two of the causes which we distinguished in our work on nature-the matter and the source of the movement-vaguely, however, and with no clearness, but as untrained men behave in fights; for they go round their opponents and often strike fine blows, but they do not fight on scientific principles, and so too these thinkers do not seem to know what they say; for it is evident that, as a rule, they make no use of their causes except to a small extent. For Anaxagoras uses reason as a deus ex machina for the making of the world, and when he is at a loss to tell from what cause something necessarily is, then he drags reason in, but in all other cases ascribes events to anything rather than to reason. And Empedocles, though he uses the causes to a greater extent than this, neither does so sufficiently nor attains consistency in their use. At least, in many cases he makes love segregate things, and strife aggregate them. For whenever the universe is dissolved into its elements by strife, fire is aggregated into one, and so is each of the other elements; but whenever again under the influence of love they come together into one, the parts must again be segregated out of each element.

"Empedocles, then, in contrast with his precessors, was the first to introduce the dividing of this cause, not positing one source of movement, but different and contrary sources. Again, he was the first to speak of four material elements; yet he does not use four, but treats them as two only; he treats fire by itself, and its opposite-earth, air, and water-as one kind of thing. We may learn this by study of his verses.

"This philosopher then, as we say, has spoken of the principles in this way, and made them of this number. Leucippus and his associate Democritus say that the full and the empty are the elements, calling the one being and the other non-being-the full and solid being being, the empty non-being (whence they say being no more is than non-being, because the solid no more is than the empty); and they make these the material causes of things. And as those who make the underlying substance one generate all other things by its modifications, supposing the rare and the dense to be the sources of the modifications, in the same way these philosophers say the differences in the elements are the causes of all other qualities. These differences, they say, are three-shape and order and position. For they say the real is differentiated only by 'rhythm and 'inter-contact' and 'turning'; and of these rhythm is shape, inter-contact is order, and turning is position; for A differs from N in shape, AN from NA in order, M from W in position. The question of movement-whence or how it is to belong to things-these thinkers, like the others, lazily neglected.

"Regarding the two causes, then, as we say, the inquiry seems to have been pushed thus far by the early philosophers.
"""



def send_messages(url, messages):
    payload = build_payload(messages)
    return send_payload(url, payload)

def send_payload(url, data):

    try:
        # Make a POST request with JSON payload
        response = requests.post(url, json=data)

        # Check if the request was successful
        response.raise_for_status()
        response.json()
        return response
    except requests.exceptions.RequestException as e:
        # Handle any exceptions that occur during the request
        print(f"Request error: {e}")

def build_payload(messages, model="llama3.2", stream=False):
    return {
        "model": "llama3.2",
        "messages": messages,
        "stream": False
    }


def add_question(messages, prompt, text):
    message = prompt + "\n\n" + text
    return add_message(messages, "user", message)


def add_message(messages, role, message):
    new_message = {
        "role": role,
        "content": message
    }
    
    messages.append(new_message)
    return messages


def text_splitter(text, chunk_size):
    """Splits the text into chunks based on sentence boundaries and returns a list."""
    text = re.sub(r'\n', ' ', text)
    sentences = re.split(r'(?<=[.!?]) +', text)
    current_chunk = ""
    chunks = []
    
    for sentence in sentences:
        if len(current_chunk) + len(sentence) + 1 <= chunk_size:
            current_chunk += sentence + " "
        else:
            if current_chunk:
                chunks.append(current_chunk.strip())
            if len(sentence) > chunk_size:
                words = sentence.split()
                current_sentence = ""
                for word in words:
                    if len(current_sentence) + len(word) + 1 <= chunk_size:
                        current_sentence += word + " "
                    else:
                        chunks.append(current_sentence.strip())
                        current_sentence = word + " "
                if current_sentence:
                    chunks.append(current_sentence.strip())
            else:
                current_chunk = sentence + " "
    if current_chunk:
        chunks.append(current_chunk.strip())
    
    return chunks

def looping_send(text_list, prompt):
    curr_chunk = 1
    messages = []

    for chunk in text_list:
        print(f"Working on chunk {curr_chunk} out of {len(text_list)}\n")
        # send_text(url, prompt, chunk)
        
        messages = add_question(messages, prompt, chunk)
        response = send_messages(api_endpoint, messages)

        json_response = response.json()
        returned_message = json_response["message"]["content"]
        print(returned_message)
        messages = add_message(messages, "assistant", returned_message)

        print(f"\nJust finished chunk {curr_chunk} out of {len(text_list)}")
        curr_chunk += 1
    return messages

def parse_responses(messages):
    out_str = ""
    for message in messages:
        if (message["role"] == "assistant"):
            out_str += "\n\n" + message["content"]
    return out_str

def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()

def write_to_file(text, filename="out.md", overwrite=True):
    mode = "w" if overwrite else "a"
    with open(filename, mode, encoding="utf-8") as file:
        file.write(text + "\n")

def dostuff(text, prompt, out_filename="out.md"):


    text_list = text_splitter(text, 6000)
    messages = looping_send(text_list, prompt)

    pprint(messages)
    
    responses_str = parse_responses(messages)

    write_to_file(responses_str, out_filename)

def main():
    parser = argparse.ArgumentParser(description="Process a prompt, an input file, and produce an output file.")
    parser.add_argument('prompt', type=str, help="The prompt text")
    parser.add_argument('input_file', type=str, help="Path to the input file")
    parser.add_argument('output_file', type=str, help="Path to the output file")

    args = parser.parse_args()

    # Read the content of the input file
    input_text = read_file(args.input_file)



    # Assign the arguments to variables
    prompt = args.prompt
    out_filename = args.output_file


    dostuff(input_text, args.prompt, args.output_file)


if __name__ == "__main__":
    main()
BASIC_PROMPT = '''Given the meme, with the Text: "{}" embedded in the image, your task is to determine whether this meme is harmful or not, in order to maintain the harmlessness and integrity of information on the Internet. Please leverage your extensive knowledge to deeply analyze and understand this meme, and give your final judgment.
Your output should stricly follow the format: "Thought: [Your analysis]\nAnswer: [harmful/harmless].'''

RSA_PROMPT = '''Given the meme, with the Text: "{}" embedded in the image, your task is to determine whether this meme is harmful or not, in order to maintain the harmlessness and integrity of information on the Internet. A classifier that can identify common features among multiple memes has labeled this meme as {}. Please review the classifier's judgment carefully and use your extensive knowledge to analyze and understand this meme before providing your final verdict. If you disagree with the classifier's judgment, you must provide exceptionally thorough and persuasive reasons.
Your output should strictly follow the format: "Thought: [Your analysis]\nAnswer: [harmful/harmless]."\n'''

llava_harmC_insights = \
'''1. Assess the overall impact of the meme, including whether it is likely to be perceived as light-hearted or offensive, especially in sensitive contexts such as health crises, disasters, social issues, or activism. Consider whether it trivializes serious situations, promotes irresponsible or dangerous behavior, spreads misinformation, or is insensitive to those affected, even if the intent is humorous.
2. Consider the context and intent of the meme, especially if it is meant to be humorous or relatable, but also weigh the potential for it to be perceived as insensitive, harmful, or misleading in serious situations.
3. Evaluate whether the meme directly or indirectly promotes harmful stereotypes, ideas, or personal attacks, trivializes serious issues or individuals’ efforts, spreads misinformation, or could be perceived as insensitive or harmful.
4. Evaluate whether the meme trivializes serious situations, issues, or the efforts of activists, which could be harmful or offensive to those affected, and consider the potential for it to spread misinformation, encourage irresponsible behavior, or be perceived as insensitive, especially in the context of public health and safety.
5. Evaluate whether the meme could potentially encourage harmful actions or behaviors, especially in the context of public health and safety. Consider the potential for it to downplay the severity of serious issues, spread misinformation, or be perceived as insensitive, even if the intent is humorous.
6. Consider the potential for the meme to spread misinformation, harmful stereotypes, or contribute to harmful narratives, even if it is intended as a joke, especially in the context of public health and safety.
7. Pay special attention to memes that reference sensitive social, political, or cultural issues, as these are more likely to be harmful.
8. Assess the potential for the meme to be interpreted in a harmful or misleading way by different audiences, considering the broader social, political, and cultural context, and the potential for it to spread misinformation or harmful narratives.
9. Evaluate the potential for the meme to be misinterpreted by different audiences, leading to harmful consequences, even if the intent is humorous, and consider the broader social and cultural context.
10. Consider the potential for the meme to be interpreted as promoting or endorsing harmful actions or behaviors, especially in the context of public health and safety.'''

llava_FHM_insights = \
'''1. Always consider the potential for double meanings, innuendos, and cultural stereotypes in the text of a meme.
2. Evaluate the context in which the meme could be shared, its intent, and its potential impact on different audiences.
3. Be cautious of memes that could be interpreted as promoting or trivializing inappropriate or harmful behavior.
4. Consider the broader social and cultural implications of the meme's content and text, while also weighing the intent, humor, and factual accuracy behind it.
5. Be sensitive to cultural stereotypes and avoid memes that could perpetuate or reinforce negative stereotypes about any group.
6. Differentiate between provocative or controversial statements and genuinely harmful content, ensuring that the meme's potential to cause real harm is the primary consideration.'''

llava_MAMI_insights = \
'''1. Always consider if the meme perpetuates stereotypes or objectifies individuals based on gender, race, or other attributes.
2. Assess if the humor or content used in the meme could be interpreted as demeaning, derogatory, or objectifying towards any group.
3. Take into account the broader social context, intent, and potential negative interpretations of the meme, distinguishing between harmful content and harmless humor.
4. Evaluate whether the meme could be perceived as trivializing or making light of serious social issues, even if the intent appears humorous.
5. Consider the use of satire, exaggeration, and wordplay in the meme and whether it is intended to provoke thought or humor rather than to harm.'''

gpt4o_harmC_insights = \
'''1. Evaluate if the humor in the meme is appropriate and does not trivialize serious issues, create unnecessary panic, target individuals or groups in a derogatory manner, or undermine critical health measures and policies, especially during ongoing crises like pandemics.
2. Consider the broader context and potential negative impact of the meme, especially in sensitive situations such as health crises or political discourse, to determine if it could cause fear, anxiety, spread misinformation, trivialize serious issues, or undermine important public health measures.
3. Identify if the meme mocks, trivializes, or undermines public health measures and policies, as this can contribute to harmful behaviors, spread misinformation, and undermine public trust in health directives and governance.
4. Ensure the meme does not encourage or normalize behavior that could be harmful in real life, particularly in the context of public health and safety, such as trivializing quarantine, policy effectiveness, or other critical health measures.
5. Assess if the meme perpetuates misinformation or undermines public health measures, which can contribute to harmful outcomes.
6. Ensure the meme does not inadvertently normalize, trivialize, or encourage harmful behaviors by presenting them humorously, especially in the context of ongoing public health issues and governance policies.
7. Recognize that memes leveraging fear-based tactics, even for promoting good behavior, can be harmful and should be scrutinized closely.
8. Assess the potential for the meme to incite derogatory or harmful sentiments towards individuals or groups, which can contribute to a negative, hostile, or unproductive environment.
9. Assess if the meme trivializes or mocks behaviors that were critical during crises (e.g., panic buying, hoarding) in a way that could diminish the perceived seriousness of the situation or encourage similar behavior in the future.
10. Determine if the meme's absurdity or exaggeration clearly indicates humor, reducing the likelihood of it being taken seriously and causing harm.'''

gpt4o_FHM_insights = \
'''1. Evaluate the context and possible interpretations of both the image and text together to determine if the meme could be harmful.
2. Use a balanced approach, considering the potential for harm while recognizing the context, intent, and humor of the meme. Clearly differentiate between harmful content and satire or light-hearted humor to avoid unnecessary censorship.
3. Assess the potential for a meme to be perceived as offensive by considering the broader context and audience, but avoid overemphasizing potential offense if the context and humor suggest a harmless or light-hearted intent.
4. Consider the use of exaggeration and satire in memes, recognizing that these elements are often used for humor. Clearly differentiate between satirical humor and content with genuine harmful intent.
5. Always consider the potential for text in a meme to be interpreted in a harmful or inappropriate manner. However, distinguish between light-hearted humor and genuinely harmful or disrespectful content.
6. Consider the broader social, cultural, and racial implications of the meme's content to assess its potential harm.
7. Differentiate between controversial or politically charged content and genuinely harmful content to prevent unnecessary censorship of opinion-based memes.
8. When evaluating memes, always consider if the content perpetuates racial, cultural, or ethnic stereotypes, as this can be harmful even if the intent seems humorous.
9. Explicitly differentiate between anthropomorphism and harmful stereotypes about people or specific groups, recognizing that portraying animals with human traits for humor is generally acceptable if it does not convey a negative or harmful message.
10. When evaluating memes, consider the historical and cultural significance of the references used, ensuring that sensitive topics are not trivialized or used inappropriately.'''

gpt4o_MAMI_insights = \
'''1. Recognize and account for humor or satire, ensuring they are not mistaken for serious harmful content. Consider the context, intent, and whether the humor directly trivializes serious subjects such as violence, sexual behavior, or perpetuates harmful stereotypes.
2. When evaluating humor, assess whether it perpetuates or trivializes harmful stereotypes, biases, serious life-threatening situations, or explicit content inappropriately. Consider the overall impact on the targeted group, while balancing this with the intent and context of the humor.
3. When identifying harmful content, evaluate the context, intent behind the language used, and the cultural nuances of humor, especially when dealing with sensitive topics.
4. Consider the potential for reinforcing harmful stereotypes, real-world harm, or incitement that the content may cause, but also recognize the difference between satire and genuinely harmful content.
5. Avoid overgeneralizing potentially divisive content as inherently harmful without further examination.
6. Consider if the meme's humor is based on sensitive or protected characteristics, and the potential negative impact it could have on those groups, especially if it reinforces harmful stereotypes or biases.
7. Evaluate whether the meme contains humor that could desensitize viewers to serious issues or dangerous situations, and consider the context and intent to determine if it amplifies potential harm.
8. Evaluate if the humor or satire presents a conflicting message that diminishes the original intent of empowering or positive content.
9. Distinguish between explicit content meant to entertain a mature audience and content genuinely intended to harm or offend, ensuring cultural and contextual humor is appropriately considered.
10. Consider whether the combination of humor and serious messages dilutes the impact of the positive message or reinforces harmful attitudes.'''


MEME_INSIGHTS = {'llava-v1.6-34b': {'harmC': llava_harmC_insights, 'FHM': llava_FHM_insights, 'MAMI': llava_MAMI_insights},
                 'gpt-4o': {'harmC': gpt4o_harmC_insights, 'FHM': gpt4o_FHM_insights, 'MAMI': gpt4o_MAMI_insights}}
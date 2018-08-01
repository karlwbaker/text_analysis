# text_analysis

A multi-phase text-analysis project to create a linguistic "Where's That From?" tool that ingests any English phrase and returns the most likely and relevant sources from which the phrase derived. Input can be audio, video, or text. Initial phases of project will support text input only.

##### Example
Input: "'sup, dog?"  
Output: Amonger other possible elements of the output, :
 - Definition and usage (formal/scientific/slang/etc.), etc.
 - Meaning of the contraction 'sup
 - Dialectical, regional, ethnic, etc. influences in the construction of the contraction
 - Etymology of the use of the word dog in a friendly greeting
 - Potential "firsts": first time phrase was used in print/song/movie/etc.
 
##### Example
Input: "Wherefore art thou?"  
Output: Most likely an allusion to Juliet speaking in Act A, Scene S, Line L, of 'Romeo and Juliet,' a play by William Shakespeare first performed at the XXX playhouse in XXX, England in [date]. Juliet is [give context, explanation, etc.].

##### Example
Input: "Jeremiah was a bullfrog I helped him a-drink his wine"  
Output: Besides the fact that these words are from the lyrics to 'Joy To The World,' a US Billboard number 1 single released by Three Dog Night in 1970 (and by others since), we all will need to wait to see what the "Where's That From?" tool finds as the etymological roots of these phrases.

# Phase 0: Implement Machine Learning Pipeline and Models Presented in _Applied Text Analysis with Python_ (O'Reilly 2018: Bengfort, Bilbro, Ojeda)

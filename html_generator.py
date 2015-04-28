#Part1: Include lecture content in the list. The first element ist just the counter of
#the lecture. The following parts are included lists which first elements provide the 
#headline of the concept and the second its content.
Input_LIST_Lecture_6 = ['Lecture 6', ['Functions (= procedure) in python', 'With a procedure you can map inputs to outputs. To define a function you have to use the expression "def". The whole function starts with a starting line including the "def", the name of the function and the inputs (Bsp.: def "name of function" (input1, input2)). After the starting line comes the body which includes the specification what to do with the parameters. At the end of the function you have to define what has to be returned. To use the function it is now just necessary to write the name of the function, followed by the defined value-parameters in brackets. Procedures can have x inputs which are also called operands or parameter or arguments. All inputs have to be used in a procedure. If a procedure has no return then it has no value and prints out "none".'],
                             ['Advantage of functions for programmers', 'With functions you can define a couple of programming steps which come over and over again. By using a function these steps can be done automatically with just one order like the definition of a DEV-Box in HTML. The individual content of the box would be defined by the parameters.']]

Input_List_Lecture_7 = ['Lecture 7', ['while-, if-, or-, and-expression', 'By using the expression while you can repeat a process until a specified condition is fulfilled.  By using the expression if you can define specific circumstances and what to do if these are fulfilled. Example: The -block- defines the steps which have to be proceeded if the condition is fulfilled. If the condition is not fulfilled then the "return xxx" line will be processed. For Boolean results you have to include the code "print True" or "print False" (with T and F as capital letters). In case of several conditions you can use an "or" (if only one needs to be fulfilled) or "and" (if all conditions have to be fulfilled). Example: If you use "or" and the first condition is already fulfilled then python will not check the second condition. Only if the first condition is false then python would print the result of the second condition. With the expression "Max(a,b,c)" you can directly evaluate the highest value of a, b and c.'],
                                       ['Loops', 'With the expression "While" you can repeat process steps over and over again. Example: As long as the test expression is true the block would be processed. If the test expression is false then the next process step after the while block will be conducted. Loops can also go forever, or at least as long as they are not stopped by the user or the computer itself due to system limitation. It is also possible to stop a look automatically even If the test expression is true by using a break time. Example:'],
                                       ['How to correct bugs', 'Bugs are part of every software development project. Hence the correction of them is part of the daily routine of every programmer. To correct bugs there are several possibilities you can use:<br>   1. Examine error messages when program crash <br>    a. The last line of python tracebacks provides information of what went wrong. If you read the message backwards then you can identify where to find the problem<br>  2. Work from example code<br>    a. If your individual code does not work then take that part out and try to use example code and which you can modify step by step until it does what you want.<br>  3. Make sure examples work<br>    a. Not all examples you find in the web are correct. You should always test example code first do ensure that it does what you want.<br>  4. Check (print) intermediate results<br>    a. If the code does not provide the expected outcome without crashing then add print statements to the program to see part results and to identify from which point on the program starts being incorrect.<br>  5. Keep and compare old versions<br>    a. Old versions of your programs should always be saved so that you always have a fall-back version. There are programs which help you with the administration of old version like Git-hub.'],
                                       ['Modular code', 'Modular code means that you separate the data from its visual presentation. The advantages are that you can change one of it without influencing the other and that is becomes easier to remain the overview of your coding. However this requires systematic thinking and a clear plan to solve the problem:<br>  - Understand the requirments of the problem by identifying the inputs and defining the outputs.<br>  - Plan an approach to solve the problem and try to break down big tasks into smaller pieces<br>  - Re-familiarize yourself with the code you have already written and which can be useful for as many parts of the problem as possible.<br>  - Write new functions to solve pieces of the bigger problems<br>  - Put all pieces together to check if the whole program works<br><br>A good example can be found in the presentation on the Udacity website under the following <a href="https://www.udacity.com/course/viewer#!/c-ud552-nd/l-3573808959/m-3655698694">link</a>.']]

Input_List_Lecture_8 = ['Lecture 8', ['Lists', 'Strings are kind of structured data which can be broken down into their characters. However they are limited to characters. Instead of strings you can use lists which are much more powerful due to the wide range of possibilities. In lists you can use all kinds of elements like strings, numbers or lists inside a list. By using indexes you can just get one element of a list.'],
                                      ['Mutation an Aliasing', 'Another big difference between strings and lists is that lists can be mutated. You can easily change the values of a list after you created it. If you replace one part of the list it still remains the same list just with a replaced element while if you redefine a variable with another string a total new variable is created. The mutation of a list can be done in two different way. First by using "append" (e.g. mylist.append(6)) and second by "+=" (e.g. mylist += [6]). If you do not want to mutate a list, just to enhance it for one procedure then you have to use the function form ""list" = "list" + [whatever]. One more big difference is that a list can be connected to two different variables. Changing a parameter by one of them would also change it for the other variable.'],
                                      ['Loops in lists', 'With the expression "for "variable" in "list"" you can create a loop function for a list. The variable gets defined in the for-expression. The following body of the function contains the coding which gets assigned to every element of the list.'],
                                      ['Index for lists', 'There are three possibilities to index the content of a list. First one is ""list".index("value")" which finds the position of a required value. If the value does not exist the output is an error. The second one is ""value" in "list"" which returns True or False. The third one is "value" not in "list" which also returns True or False.'],
                                      ['How to solve problems', 'If you want to automate a process with a program it is quite normal that there are complex problems to solve. So do not panic and proceed in a structured way. All programs have input parameters which have relationships with each other and desired outputs. So the first step is to clarify what is the set of valid input parameters. Then you have to clarify what is the desired output. For a better understanding it makes sense to work on some examples how the program should work under specific conditions. Afterwards you should write down the structure as pseudo code (e.g. if this, then that, else something). Keep an eye on finding simple mechanical solutions. Afterwards you can start with coding.']]

#Part2: Specification of HTML layout for lecture:
def generate_lecture (lecture_title):
    html_text_1 = '''
  <div class ="lecture">
    <h2>'''+lecture_title+'''</h2>
    
    <div class="container">'''
    return html_text_1

#Part3: Variable for end-coding of lecture.
end_lecture ='''
    </div>
  </div>'''

#Part4: Coding for the concept-title and -content HTML.
def generate_concept_HTML(concept_title, concept_content):
    html_text_2 = '''

      <div class="concept">
        <div class="concept-title">
          <h3>''' + concept_title + '''</h3>'''
    html_text_3 = '''
        </div>
        <div class="concept-content">
          <p>
             '''+concept_content + '''
          </p>'''
    html_text_4 = '''
        </div>
      </div>'''
    full_html_text = html_text_2 + html_text_3 + html_text_4
    return full_html_text

#Part5: Procedure to fill in the individual content for one concept.
def make_HTML(concept):
    concept_title = concept[0]
    concept_content = concept[1]
    return generate_concept_HTML(concept_title, concept_content)

#Part6: Procedure to fill in the individual content for all concepts.
def make_HTML_for_many_concepts(list_of_concepts):
    lecture_title = list_of_concepts.pop(0)
    HTML = ""
    for concept in list_of_concepts:
        concept_HTML = make_HTML(concept)
        HTML = HTML + concept_HTML
    return generate_lecture (lecture_title) + HTML + end_lecture


print make_HTML_for_many_concepts(Input_LIST_Lecture_6)
print make_HTML_for_many_concepts(Input_LIST_Lecture_7)
print make_HTML_for_many_concepts(Input_LIST_Lecture_8)
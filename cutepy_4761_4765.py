# Konstantinos Papadopoulos AM : 4761 username: cse94761
# Ilias Papathanasiou AM : 4765 username: cse94765


import sys
global quadCounter 
quadCounter = 0

class Token :
    family_types = ["Alphabetical", "Keyword", "Number", "Underscore", "AddOper", "MulOper", "RelOp", "Assign", "Delimiter", "Group_Symbol", "Comment", "End Of File"]
    
    def __init__(self, recognized_string, family, line_number) :
        self.recognized_string = recognized_string
        self.family = self.family_types[family]
        self.line_number = line_number
        
    
class Lex :
    file_name = ""
    state = 0
    global keyword
    keyword = ["while", "if", "True", "False", "else", "return", "print", "#declare", "def"]
    point_char = 0    


    def __init__(self, input_str, current_line) :
        self.input_str = input_str
        self.current_line = current_line
    
    
    def my_print(self,token) :
        print(token.recognized_string,  " family: " , token.family , " line: " , token.line_number)  
    
    def analyze(self) -> Token:
        global point_char
        state = 0
        my_phrase = ""
        with open(self.input_str, 'r') as file:
            while True :
                file.seek(self.point_char)
                char = file.read(1)
                match state :

                    case  0 :
                        if char.isspace() :
                            state = 0
                            self.point_char += 1
                            if char == '\n' :
                                self.current_line += 1
                                 

                        elif char.isalpha() :
                            self.point_char += 1
                            my_phrase += char
                            state = 1

                        elif char.isdigit() :
                            my_phrase += char
                            self.point_char += 1
                            state = 2
                        
                        elif char == "_" :
                            self.point_char += 1
                            token = Token(char, 3, self.current_line)
                            self.my_print(token)       
                            return token
                        
                        elif char == '-' :
                            self.point_char += 1
                            token = Token(char, 4, self.current_line)
                            self.my_print(token)  
                            return token
                        
                        elif char == '+' :
                            self.point_char += 1
                            token = Token(char, 4, self.current_line)       
                            self.my_print(token)  
                            return token
                        
                        elif char == '*' :
                            self.point_char += 1
                            token = Token(char, 5, self.current_line)       
                            self.my_print(token)  
                            return token

                        elif char == '/' :
                            my_phrase += char
                            state = 3
                            self.point_char += 1

                        elif char == '<' :
                            state = 4
                            my_phrase += char
                            self.point_char += 1

                        elif char == '>' :
                            state = 5
                            my_phrase += char
                            self.point_char += 1

                        elif char == '!' :
                            state = 6
                            my_phrase += char
                            self.point_char += 1
                        
                        elif char == '=' :
                            state = 7
                            my_phrase += char
                            self.point_char += 1

                        elif char == ';' :
                            self.point_char += 1
                            token = Token(char, 8, self.current_line)   
                            self.my_print(token)  
                            return token

                        elif char == ',' :
                            self.point_char += 1
                            token = Token(char, 8, self.current_line)       
                            self.my_print(token)  
                            return token

                        elif char == ':' :
                            self.point_char += 1
                            token = Token(char, 8, self.current_line)       
                            self.my_print(token)  
                            return token

                        elif char == '[' :
                            state = 0
                            self.point_char += 1
                            token = Token(char, 9, self.current_line)       
                            self.my_print(token)  
                            return token
                        
                        elif char == ']' :
                            state = 0
                            self.point_char += 1
                            token = Token(char, 9, self.current_line) 
                            self.my_print(token)  
                            return token   

                        elif char == '(' :
                            state = 0
                            self.point_char += 1
                            token = Token(char, 9, self.current_line)       
                            self.my_print(token)  
                            return token
                        
                        elif char == ')' :
                            state = 0
                            self.point_char += 1
                            token = Token(char, 9, self.current_line)
                            self.my_print(token)  
                            return token
                        
                        elif char == '#' :
                            declare_counter = 0
                            state = 8       
                            my_phrase += char    
                            self.point_char += 1
                        
                        elif not char :
                            token = Token("End Of File", 11, self.current_line)
                            self.my_print(token)  
                            return token
                        
                        else :
                            sys.exit("Unrecognized character found!")

                    case 1 :
                        if (char.isalpha() or char.isdigit() or char == '_') :
                            my_phrase += char
                            state = 1
                            self.point_char += 1
                            if len(my_phrase) > 30 :
                                sys.exit("Inserted variable lenght out of bounds!")
                            
                        else :
                            state = 0
                            if my_phrase in keyword :
                                token = Token(my_phrase, 1, self.current_line)   
                                self.my_print(token)      
                                return token
                            else :
                                token = Token(my_phrase, 0, self.current_line) 
                                self.my_print(token)
                                return token

                    case 2 :
                        if char.isdigit() :
                            my_phrase += char
                            state = 2
                            self.point_char += 1 
                            if int(my_phrase) < -((2**32) -1) or int(my_phrase) > ((2**32) -1) :
                                sys.exit("Inserted number out of bounds!")
                        else :
                            state = 0
                            token = Token(my_phrase, 2, self.current_line)
                            self.my_print(token)  
                            return token
                    
                        
                    case 3 :
                        if char == '/' :
                            my_phrase += char
                            self.point_char += 1
                            state = 0 
                            token = Token(my_phrase, 5, self.current_line)
                            self.my_print(token)  
                            return token
                        else : 
                            sys.exit("Expected '/' !")
                    
                    case 4 :
                        if char == '=' :
                            my_phrase += char
                            self.point_char += 1
                            state = 0
                            token = Token(my_phrase, 6, self.current_line) 
                            self.my_print(token)        
                            return token
                        else :
                            state = 0
                            token = Token(my_phrase, 6, self.current_line)    
                            self.my_print(token)     
                            return token 
                                           
                    case 5 :
                        if char == '=' :
                            my_phrase += char
                            self.point_char += 1
                            state = 0
                            token = Token(my_phrase, 6, self.current_line)    
                            self.my_print(token)     
                            return token
                        else :
                            state = 0
                            token = Token(my_phrase, 6, self.current_line) 
                            self.my_print(token)        
                            return token
                        
                    case 6 :
                        if char == '=' :
                            my_phrase += char
                            self.point_char += 1
                            state = 0
                            token = Token(my_phrase, 6, self.current_line) 
                            self.my_print(token)  
                            return token      
                        else :
                            sys.exit("Expected '=' !")

                    case 7 :
                        state = 0
                        if char == '=' :
                            my_phrase += char
                            self.point_char += 1
                            token = Token(my_phrase, 6, self.current_line) 
                            self.my_print(token)  
                            return token      
                        else :
                            token = Token(my_phrase, 7, self.current_line)  
                            self.my_print(token)  
                            self.point_char += 1 
                            return token
            
                    case 8 :                        
                        if char == '$' :
                            my_phrase += char
                            self.point_char += 1
                            state = 0
                            token = Token(my_phrase, 10 , self.current_line)
                            self.my_print(token)  
                            return token
                        elif char == '{' :
                            my_phrase += char
                            self.point_char += 1
                            state = 0
                            token = Token(my_phrase, 9 , self.current_line)
                            self.my_print(token)  
                            return token
                        elif char == '}' :
                            my_phrase += char
                            self.point_char += 1
                            state = 0
                            token = Token(my_phrase, 9 , self.current_line)
                            self.my_print(token)  
                            return token
                        elif char.isalpha() :
                            declare_counter += 1
                            my_phrase += char
                            self.point_char += 1
                            state = 8
                            if declare_counter == 7 :
                                if my_phrase == "#declare" :
                                    token = Token(my_phrase, 1 , self.current_line)
                                    self.my_print(token)  
                                    state = 0
                                    return token
                                else :
                                    sys.exit("Expected declare after the # ! ")        
                        else :
                            sys.exit("Expected either '$' or '{' or '}' ! ")
      


class Syntax_Analyzer :
    
    current_line = 0
    input_file = ""

    my_lex = Lex(None,None)
    
    def __init__(self, this_input_file, lexical_analyzer):
        self.input_file = this_input_file
        self.my_lex = lexical_analyzer
        self.token = Token(None, 0, None)    


    def get_token(self) :
        self.token = self.my_lex.analyze()
        return self.token

    def start_rule(self) :
        print("Compiling code...")
        print("-------------------------------------------------------------------------------------------------------------------------------------")
        self.token = self.get_token()
        if  self.token.recognized_string == "def" :
            self.def_main_part() 
            if self.token.recognized_string == "if" :
                self.call_main_part()
            elif self.token.recognized_string == "def" :
                sys.exit("Cannot define a main function at this point!")
            else :
                sys.exit("Invalid program syntax. Missing the call of at least one main function!")
        else :
            sys.exit("Invalid function call! \n The start of a program should be a definition of a main function!")

    def def_main_part(self):
        while self.token.recognized_string == "def" :
            self.token = self.get_token()
            self.def_main_function()


    def def_main_function(self) :
        if self.token.recognized_string in keyword :
            sys.exit("Invalid variable name inside function definition! \n Variable name shouldn't be a keyword!")
        
        if self.token.family == "Alphabetical" :
            self.token = self.get_token()
            if self.token.recognized_string == "(" :
                self.token = self.get_token()
                if self.token.recognized_string == ")" :
                    self.token = self.get_token()
                    if self.token.recognized_string == ":" :
                        self.token = self.get_token()
                        if self.token.recognized_string == "#{" :
                            self.token = self.get_token()
                            self.declarations()
                            while self.token.recognized_string == "def" :
                                self.token = self.get_token()
                                self.def_function()
                            self.statements()
                            if self.token.recognized_string == "#}" :
                                self.token = self.get_token()
                            else :
                                sys.exit("Invalid definition of main function! \n '#}' expected!")
                        else :
                            sys.exit("Invalid definition of main function! \n Main functions should start with '#{'!")
                    else :
                        sys.exit("Invalid definition of main function! \n ':' expected!")
                else :
                    sys.exit("Invalid definition of main function! \n ')' expected!")
            else :
                sys.exit("Invalid definition of main function! \n '(' expected!")
        else :
            sys.exit("Invalid definition of main function! \n Main functions should start with a letter!")                    


    def def_function(self) :
        if self.token.recognized_string in keyword :
            sys.exit("Invalid variable name inside function definition! \n Variable name shouldn't be a keyword!")
        if self.token.family == "Alphabetical" :
            self.token = self.get_token()
            if self.token.recognized_string == "(" :
                self.token = self.get_token()
                self.idlist()
                if self.token.recognized_string == ")" :
                    self.token = self.get_token()
                    if self.token.recognized_string == ":" :
                        self.token = self.get_token()
                        if self.token.recognized_string == "#{" :
                            self.token = self.get_token()
                            self.declarations()
                            while self.token.recognized_string == "def" :
                                self.token = self.get_token()
                                self.def_function()
                            self.statements()
                            if self.token.recognized_string == "#}" :
                                self.token = self.get_token()
                            else :
                                sys.exit("Invalid definition of function! \n '#}' expected!")
                        else :
                            sys.exit("Invalid definition of function! \n Main functions should start with '#{'!")
                    else :
                        sys.exit("Invalid definition of function! \n ':' expected!")
                else :
                    sys.exit("Invalid definition of function! \n ')' expected!")
            else :
                sys.exit("Invalid definition of function! \n '(' expected!")
        else :
            sys.exit("Invalid definition of function! \n Functions should start with a letter!")                            
    
    def declarations(self) :
        while self.token.recognized_string == "#declare":
            self.declaration_line()

    def declaration_line(self) :
        if self.token.recognized_string == "#declare":
            self.token = self.get_token() 
            self.idlist()
        else :
            sys.exit("Invalid declaration syntax inside declaration line!")
        
    def statement(self) :
        if self.token.recognized_string == "if" or self.token.recognized_string == "while" :
            self.structured_statement()
        elif self.token.recognized_string == "print" or self.token.recognized_string == "return" or self.token.family == "Alphabetical" :
            self.simple_statement()
        else :
            sys.exit("Invalid statement syntax! \n Expected either a simple or a structured statement!")
        

    def statements(self) :
        self.statement()
        while self.token.recognized_string == "if" or self.token.recognized_string == "while" or self.token.recognized_string == "print" or self.token.recognized_string == "return" or self.token.family == "Alphabetical"  :
            self.statement()
        

    def simple_statement(self) :
        if self.token.recognized_string == "print" :
            self.print_stat()
        elif self.token.recognized_string == "return" :
            self.return_stat()
        elif self.token.family == "Alphabetical" :
            if self.token.recognized_string in keyword :
                sys.exit("Invalid variable name inside simple statement! \n Variable name shouldn't be a keyword!")
            else :
                self.assignement_stat()
        else :
            sys.exit("Invalid simple statement syntax!")

    def structured_statement(self) :
        if self.token.recognized_string == "if" :
            self.if_stat()
        elif self.token.recognized_string == "while" :
            self.while_stat()
        else :
            sys.exit("Invalid structured statement syntax!")

    def assignement_stat(self) :
        self.token = self.get_token()
        if self.token.recognized_string == "=" :
            self.token = self.get_token()
            if self.token.recognized_string == "int" :
                self.token = self.get_token()
                if self.token.recognized_string == "(" :
                    self.token = self.get_token()
                    if self.token.recognized_string == "input" :
                        self.token = self.get_token()
                        if self.token.recognized_string == "(" :
                            self.token = self.get_token()
                            if self.token.recognized_string == ")" :
                                self.token = self.get_token()
                                if self.token.recognized_string == ")" :
                                    self.token = self.get_token()
                                    if self.token.recognized_string == ";" :
                                        self.token = self.get_token()
                                    else :
                                        sys.exit("Invalid simple statement syntax! \n Simple statements should end with ';'!")
                                else :
                                    sys.exit("Invalid simple statement syntax! \n ')' expected!")
                            else :
                                    sys.exit("Invalid simple statement syntax! \n ')' expected!")
                        else :
                            sys.exit("Invalid simple statement syntax! \n '(' expected!")
                    else :
                        sys.exit("Invalid simple statement syntax! \n 'input' expected!")
                else :
                    sys.exit("Invalid simple statement syntax! \n '(' expected!")
            else :
                self.expression()
                if not self.token.recognized_string == ";" :
                    sys.exit("Invalid simple statement syntax! \n Simple statements should end with ';'!")
                self.token = self.get_token()
        else :
            sys.exit("Invalid simple statement syntax!")
                
        
    def print_stat(self) :
        self.token = self.get_token()
        if self.token.recognized_string == "(" :
            self.token = self.get_token()
            self.expression()
            if self.token.recognized_string == ")" :
                self.token = self.get_token()
                if self.token.recognized_string == ";" :
                    self.token = self.get_token()
                else :
                    sys.exit("Invalid print statement syntax! \n ';' expected!")
            else :
                sys.exit("Invalid print statement syntax! \n ')' expected!")
        else :
            sys.exit("Invalid print statement syntax! \n '(' expected!")
        

    def return_stat(self) :
        self.token = self.get_token()
        if self.token.recognized_string == "(" :
            self.token = self.get_token()
            self.expression()
            if self.token.recognized_string == ")" :
                self.token = self.get_token()
                if self.token.recognized_string == ";" :
                    self.token = self.get_token()
                else :
                    sys.exit("Invalid return statement syntax! \n ';' expected!")
            else :
                sys.exit("Invalid return statement syntax! \n ')' expected!")
        else :
            sys.exit("Invalid return statement syntax! \n '(' expected!")
            

    def if_stat(self) :
        self.token = self.get_token()
        if self.token.recognized_string == "(" :
            self.token = self.get_token()
            self.condition()
            if self.token.recognized_string == ")" :
                self.token = self.get_token()
                if self.token.recognized_string == ":" :
                    self.token = self.get_token()
                    if self.token.recognized_string == "#{" :
                        self.token = self.get_token()
                        self.statements()
                        if self.token.recognized_string == "#}" :
                            self.token = self.get_token()
                            if self.token.recognized_string == "else" :
                                self.token = self.get_token()
                                if self.token.recognized_string == ":" :
                                    self.token = self.get_token()
                                    if self.token.recognized_string == "#{" :
                                        self.token = self.get_token()
                                        self.statements()
                                        if self.token.recognized_string == "#}" :
                                            self.token = self.get_token()
                                        else :
                                            sys.exit("Invalid else syntax! \n '#}' expected!")
                                    else :
                                        self.statement()
                                else :
                                    sys.exit("Invalid else syntax! \n ':' expected!")                                
                            else :
                                pass
                        else :
                            sys.exit("Invalid if syntax! \n '#}' expected!")
                    else :
                        self.statement()
                        if self.token.recognized_string == "else" :
                                self.token = self.get_token()
                                if self.token.recognized_string == ":" :
                                    self.token = self.get_token()
                                    if self.token.recognized_string == "#{" :
                                        self.token = self.get_token()
                                        self.statements()
                                        if self.token.recognized_string == "#}" :
                                            self.token = self.get_token()
                                        else :
                                            sys.exit("Invalid else syntax! \n '#}' expected!")
                                    else :
                                        self.statement()
                                else :
                                    sys.exit("Invalid else syntax! \n ':' expected!")
                else :
                    sys.exit("Invalid if syntax! \n ':' expected!")
            else :
                sys.exit("Invalid if syntax! \n ')' expected!")
        else :
            sys.exit("Invalid if syntax! \n '(' expected!")
            
    def while_stat(self) :
        self.token = self.get_token()
        if self.token.recognized_string == "(" :
            self.token = self.get_token()
            self.condition()
            if self.token.recognized_string == ")" :
                self.token = self.get_token()
                if self.token.recognized_string == ":" :
                    self.token = self.get_token()
                    if self.token.recognized_string == "#{" :
                        self.token = self.get_token()
                        self.statements()
                        if self.token.recognized_string == "#}" :
                            self.token = self.get_token()
                        else :
                            sys.exit("Invalid while syntax! \n '#}' expected!")
                    else :
                        self.statement()
                else :
                    sys.exit("2:Invalid while syntax! \n ':' expected!")
            else :
                sys.exit("3:Invalid while syntax! \n ')' expected!")
        else :
            sys.exit("Invalid while syntax! \n '(' expected!")


    def idlist(self) :
        if self.token.family in keyword :
            sys.exit("Invalid variable name in idlist syntax! \n Variable name should not be a keyword!")

        elif self.token.family == "Alphabetical":
            self.token = self.get_token()
            while self.token.recognized_string == "," :
                self.token = self.get_token()
                if self.token.recognized_string in keyword :
                    sys.exit("Invalid variable name in idlist syntax! \n Variable name should not be a keyword!")        
                if self.token.family == "Alphabetical" :
                    self.token = self.get_token()
                else :
                    sys.exit("Invalid kleene star in idlist syntax! \n ID expected after comma!")
        else :
            pass   

    def expression(self) :
        self.optional_sign()
        self.term()
        while self.token.family == "AddOper" : 
            self.token = self.get_token()
            self.term()

    def term(self) :
        self.factor()
        while self.token.family == "MulOper" :
            self.token = self.get_token()
            self.factor()

    def factor(self) :
        if self.token.family == "Number" :
            self.token = self.get_token()

        elif self.token.recognized_string == "(" :
            self.token = self.get_token()
            self.expression()
            if self.token.recognized_string == ")" :
                self.token = self.get_token()
            else :
                sys.exit("Invalid syntax of factor! \n ')' expected!")

        elif self.token.recognized_string in keyword :
            sys.exit("Invalid variable name inside factor! \n Variable name should not be a keyword!")

        elif self.token.family == "Alphabetical":
            self.token = self.get_token() 
            self.idtail()
                
    def idtail(self) :
        if self.token.recognized_string == "(" :
            self.token = self.get_token()
            self.actual_par_list()
            if self.token.recognized_string == ")" :
                self.token = self.get_token()
            else :
                sys.exit("Invalid syntax of idtail! \n ')' expected!")
            
        else :
            pass

    def actual_par_list(self) :
        if self.token.recognized_string == ")" :
            pass
        else :
            self.expression()
            while self.token.recognized_string == "," :
                self.token = self.get_token()
                self.expression()
          
    def optional_sign(self) :
        if self.token.family == "AddOper" :
            self.token = self.get_token()

        else :
            pass
        
    def condition(self) :
        self.bool_term()
        while self.token.recognized_string == "or" :
            self.token = self.get_token()
            self.bool_term()

    def bool_term(self) :
        self.bool_factor()
        while self.token.recognized_string == "and" : 
            self.token = self.get_token()
            self.bool_factor()

    def bool_factor(self) : 
        if self.token.recognized_string == "not" :
            self.token = self.get_token() 
            if self.token.recognized_string == "[" :
                self.token = self.get_token() 
                self.condition()
                if self.token.recognized_string == "]" :
                    self.token = self.get_token()                 
                else :
                    sys.exit("Invalid syntax in boolean factor! \n ']' expected'!")
                
            else :
                sys.exit("Invalid syntax in boolean factor! \n '[' expected'!")

        elif self.token.recognized_string == "[" :
                self.token = self.get_token() 
                self.condition()
                if self.token.recognized_string == "]" :
                    self.token = self.get_token()                 
                else :
                    sys.exit("Invalid syntax in boolean factor! \n ']' expected'!")
            
        else  :
            self.expression()
            if self.token.family == "RelOp" :
                self.token = self.get_token() 
                self.expression()
            else :
                sys.exit("Invalid boolean factor syntax! \n Expected a relational operator")
    
    def call_main_part(self) :
        if self.token.recognized_string == "if" :
            self.token = self.get_token()
            if self.token.recognized_string == "_" :
                self.token = self.get_token()
                if self.token.recognized_string == "_" :
                    self.token = self.get_token()
                    if self.token.recognized_string == "name__" :
                        self.token = self.get_token()
                        if self.token.recognized_string == "==" :
                            self.token = self.get_token()
                            if self.token.recognized_string == "_" :
                                self.token = self.get_token()
                                if self.token.recognized_string == "_" :
                                    self.token = self.get_token()
                                    if self.token.recognized_string == "main__" :
                                        self.token = self.get_token()
                                        if self.token.recognized_string == ":" :
                                            self.token = self.get_token()
                                            self.token = self.get_token()
                                            self.main_function_call()                                            
                                            while self.token.recognized_string.startswith("main_") :
                                                self.token = self.get_token()
                                                self.main_function_call()
                                            print("-------------------------------------------------------------------------------------------------------------------------------------")
                                            sys.exit("Compilation completed successfully!")
                                        else :
                                            sys.exit("Invalid syntax when calling main part! \n ':' expected!")
                                    else :
                                        sys.exit("Invalid syntax when calling main part! \n '__main__' expected!")
                                else :
                                    sys.exit("Invalid syntax when calling main part! \n '__main__' expected!")
                            else :
                                sys.exit("Invalid syntax when calling main part! \n '__main__' expected!")
                        else :
                            sys.exit("Invalid syntax when calling main part! \n '==' expected!")
                    else :
                        sys.exit("Invalid syntax when calling main part! \n '__name__' expected!")
                else :
                    sys.exit("Invalid syntax when calling main part! \n '__name__' expected!")
            else :
                sys.exit("Invalid syntax when calling main part! \n '__name__' expected!")
        else :
            sys.exit("Invalid syntax when calling main part! \n 'if' expected! ")
    
    def main_function_call(self) :
        if self.token.recognized_string == '(' :
            self.token = self.get_token()
            if self.token.recognized_string == ')' :
                self.token = self.get_token()
                if self.token.recognized_string == ';' :
                    self.token = self.get_token()
                    if self.token.recognized_string == "End Of File" :
                        print("-------------------------------------------------------------------------------------------------------------------------------------")
                        sys.exit("Compilation completed successfully!")
                    else :
                        pass
                else :
                    sys.exit("Invalid syntax when calling main function! \n ';' expected!")
            else :
                sys.exit("Invalid syntax when calling main function! \n ')' expected!")
        else :
             sys.exit("Invalid syntax when calling main function! \n '(' expected!")

             
class Quad :
    
    def __init__(self, operator, oper1, oper2, oper3) :
        self.operator = operator
        self.oper1 = oper1
        self.oper2 = oper2
        self.oper3 = oper3
    

class QuadPointer :
    def __init__(self) :
        self.pointerHashMap = {}

    def addToHashMap(self, key, value) :
        self.pointerHashMap[key] = value


class IntermediateCode :
    counter = 0 

    def genQuad(self, operator, oper1, oper2, oper3) -> Quad :
        newQuad = Quad(operator, oper1, oper2, oper3)
        return newQuad
    
    def backPatch(self, listOfQuad, nextLabel) :
        for quad in listOfQuad :
            quad.oper3 = nextLabel

    def nextQuad() -> int:
        return pointer.label + 1 
    
    def newTemp(cls) -> str :
        cls.counter += 1
        return f"T_{cls.counter}"
    
    def emptyList() -> list:
        quadPointerList = []
        return quadPointerList

    def makeList(x) -> list :
        newQuadPointerList = [x]
        return newQuadPointerList
    
    def merge(list1, list2) -> list:
        extendedList = list1 + list2
        return extendedList
    
    


if __name__ == '__main__' :
    if len(sys.argv) < 2 :
        print("The format is 'python 'cutepy_4761_4765'.py 'test_file'.cpy !'")
        sys.exit(1)

    input_file = sys.argv[1]
    my_lex = Lex(input_file,1)
    my_parser = Syntax_Analyzer(input_file, my_lex)
    my_parser.start_rule()
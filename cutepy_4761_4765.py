# Konstantinos Papadopoulos AM : 4761 username: cse94761
# Ilias Papathanasiou AM : 4765 username: cse94765


import sys
from abc import ABC

quadCounter = 0
quad_length_list = 1

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
      
             
class Quad :
    
    def __init__(self, operator, oper1, oper2, oper3) :
        self.operator = operator
        self.oper1 = oper1
        self.oper2 = oper2
        self.oper3 = oper3
    

class QuadPointer :
    def __init__(self) :
        self.pointerHashMap = {}

    def addToHashMap(self, quad_counter, quad) :
        self.pointerHashMap[quad_counter] = quad

    def get_Quad(self, quad_counter) :
        return self.pointerHashMap[quad_counter]


class IntermediateCode :
    counter = 0 

    def __init__(self) -> None:
        self.quad_pointer = QuadPointer()
        self.inter_code_list : list[Quad] = [] 

    def genQuad(self, operator, oper1, oper2, oper3) :
        newQuad = Quad(operator, oper1, oper2, oper3)
        global quadCounter 
        quadCounter += 1 
        self.quad_pointer.addToHashMap(quadCounter, newQuad)
        self.inter_code_list.append(newQuad)
    
    def backPatch(self, listOfQuad, nextLabel) :
        the_quad = self.quad_pointer.get_Quad(listOfQuad[0])
        the_quad.oper3 = nextLabel

    def nextQuad(self) -> int:
        return  quadCounter + 1 
    
    def newTemp(self, cls) -> str :
        cls.counter += 1
        return f"T_{cls.counter}"
    
    def emptyList(self) -> list:
        quadPointerList = []
        return quadPointerList

    def makeList(self, x : int) -> list :
        newQuadPointerList = [x]
        return newQuadPointerList
    
    def merge(self, list1, list2) -> list:
        extendedList = list1 + list2
        return extendedList
    

class Entity(ABC) :
    def __init__(self, name) -> None:
        self.name = name



class Variable(Entity) :
    def __init__(self, name, datatype, offset) -> None :
        super().__init__(name)
        self.datatype = datatype
        self.offset = offset
        self.type = "Variable"


class FormalParameter(Entity) : 
    def __init__(self, name, datatype, mode) -> None:
        super().__init__(name)
        self.datatype = datatype
        self.mode = mode
        self.type = "FormalParameter"


class Parameter(Variable) :
    def __init__(self, name, datatype, offset, mode) -> None:
        Variable.__init__(self, name, datatype, offset)
        self.mode = mode
        self.type = "Parameter"


class Function : 
    def __init__(self, name, datatype, starting_quad, frame_length, formal_parameters : list) -> None:
        self.name = name
        self.datatype = datatype
        self.starting_quad = starting_quad
        self.frame_length = frame_length
        self.formal_parameters : list = formal_parameters
        


class TemporaryVariable(Variable) :
    def __init__(self, name, datatype, offset) -> None:
        super().__init__(name, datatype, offset)
        self.type = "TemporaryVariable"
        

class SymbolicConstant(Entity) :
    def __init__(self, name, datatype, value) -> None:
        super().__init__(name)
        self.datatype = datatype
        self.value = value
        

class Scope :
    def __init__(self, level) -> None:
        self.level = level
        self.standard_offset = 12
        self.entities : list[Entity] = []
        
    def addEntityScope(self, entity) :
        self.entities.append(entity)


class Table :
    def __init__(self) :
        self.level = 0    
        self.first_scope = Scope(self.level)
        self.scopes: list[Scope]= [self.first_scope]  
    
    def getCurrentScope(self) -> Scope :
        return self.scopes[-1]
    
    def addScope(self) :
        self.level += 1
        new_scope = Scope(self.level)
        self.scopes.append(new_scope)
        
    def deleteScope(self, level) :
        for scope in self.scopes :
            if scope.level == level :
                self.scopes.remove(scope)
                self.level -= 1

    def addEntityTable(self, ent_name : str, ent_type) :
        if ent_type == "Variable" :
            new_var = Variable(ent_name, "Integer", None,)
        elif ent_type == "Function" :
            formal_parameters  = []
            new_var = Function(ent_name, "Integer", None, None, formal_parameters)
        elif ent_type == "TempVariable" :
            new_var = TemporaryVariable(ent_name, "Integer", None)
        elif ent_type == "Parameter" :
            new_var = Parameter(ent_name, "Integer", 0, "CV")
        else :
            ValueError("Invalid entity type!")
        self.getCurrentScope().addEntityScope(new_var)
     
    def updateFields(self, ent_name, datatype = None, offset = None, starting_quad = None, frame_length = None, mode = None) :
        if starting_quad is not None or frame_length is not None :
            if ent_name.startswith("main") :
                for i in range(0, len(self.scopes[self.level].entities), 1) :
                    if  self.scopes[self.level].entities[i].name == ent_name :  
                        if starting_quad is not None : 
                            self.scopes[self.level].entities[i].starting_quad = starting_quad
                        if frame_length is not None :
                            self.scopes[self.level].entities[i].frame_length = frame_length 
            else :
                func_scope = self.level -1
                for i in range(0, len(self.scopes[func_scope].entities), 1) :
                    if  self.scopes[func_scope].entities[i].name == ent_name :  
                        if starting_quad is not None : 
                            self.scopes[func_scope].entities[i].starting_quad = starting_quad
                        if frame_length is not None :
                            self.scopes[func_scope].entities[i].frame_length = frame_length 
        else :
            for i in range(0, len(self.getCurrentScope().entities), 1) :
                if  self.getCurrentScope().entities[i].name == ent_name :   
                    if datatype is not None :
                        self.getCurrentScope().entities[i].datatype = datatype
                    if offset is not None :
                        self.getCurrentScope().entities[i].offset = offset
                    if mode is not None :
                        self.getCurrentScope().entities[i].mode = mode

    def addFormalParameter(self, parameter) :
       new_formal = FormalParameter(parameter, "Integer", "CV")
       func_scope = self.getCurrentScope().level - 1
       self.scopes[func_scope].entities[-1].formal_parameters.append(new_formal)
            
    def searchForEntry(self, ent_name) :
        for scope in reversed(self.scopes):
            for entity in reversed(scope.entities) :
                    if entity.name == ent_name :
                        return entity, scope.level  

class FinalCode :
    global words

    def __init__(self, table : Table ) -> None:
        self.symb_table = table
        self.final_code_res = ""


    def produce(self, str_inp) :
        with open("final_code.asm","a") as append:
            append.write(str_inp)


    def gnlvcode(self, variable):
        res = self.symb_table.searchForEntry(variable)
        entity = res[0]
        level = res[1]
        t = 1
        self.produce("\tlw t0,-4(sp) \n")
        while (t < (abs(int(self.symb_table.getCurrentScope().level) - int(level)))) :
            self.produce("\tlw t0,-4(t0) \n")
            t += 1 
        self.produce("\taddi t0, t0," + "-" + str(entity.offset) + "\n")



    def loadvr(self, variable : str, register) :
        if (variable.isdigit()) :
            self.produce("\tli " + register + ", " + variable + "\n")
        else :
            res = self.symb_table.searchForEntry(variable)
            entity = res[0]
            level = res[1]
            if level == self.symb_table.getCurrentScope().level :
                self.produce("\tlw " + register + ",-" + str(entity.offset) + "(sp)" + "\n")
            elif ((level != self.symb_table.getCurrentScope().level) and (entity.type =="Parameter:" or entity.type == "Variable:")):
                self.gnlvcode(variable)
                self.produce("\tlw " + register + ",(t0)\n")
            elif level == 0 :
                self.produce("\tlw " + register + ",-" + str(entity.offset) +"(gp)\n")


    def storerv(self, register, variable) :
        res = self.symb_table.searchForEntry(variable)
        entity = res[0]
        level = res[1]
        if level == self.symb_table.getCurrentScope().level :
            self.produce("\tsw " + register + ",-" + str(entity.offset) + "(sp)\n")
        elif level == 0 :
            self.produce("\tsw " + register + ",-" + str(entity.offset) +"(gp)\n")
        else :         
            self.gnlvcode(variable)
            self.produce("\tsw t0,-" + str(entity.offset) + "(sp)\n")


class Syntax_Analyzer :
    global out_str , new_list
    global func_name_list, id_name
    out_str = ""
    func_name_list = []
    id_name = ""
    current_line = 0
    input_file = ""
    output_code = ""
    output_symbol_table = ""
    keep_line = 0 
    first_data_entry = True
    is_inverted = False 
    func_numbers = 0

    my_lex = Lex(None,None)
    inter_code = IntermediateCode()
    symbol_table = Table()
    final_code = FinalCode(symbol_table)

    
    def __init__(self, this_input_file, lexical_analyzer):
        self.input_file = this_input_file
        self.my_lex = lexical_analyzer
        self.token = Token(None, 0, None)    

    def get_token(self) :
        self.token = self.my_lex.analyze()
        return self.token
    
    def write_quad_to_file(self, counter : int, quad : Quad) :
        result = str(counter) + ": " + quad.operator + " " + str(quad.oper1) + " " + str(quad.oper2) + " " + str(quad.oper3) + "\n"
        return result
    
    def write_symbol_to_file(self, level : int) :
        if (self.symbol_table.scopes[level].entities[0].name.startswith("main")) :
            result = "\nScope: " + str(level) + "\t" + self.symbol_table.scopes[level].entities[0].name + "\n"
        else :
            result = "\nScope: " + str(level)  + "\t" + str(self.symbol_table.scopes[level - 1].entities[-1].name) + "\n" 
        for entity in self.symbol_table.scopes[level].entities :
            if (type(entity) == Variable):
                result += "\tVariable: " + entity.name + "\t\t" + "Offset: " + str(entity.offset) + "\n"
            if (type(entity) == Parameter) :
                result += "\tParameter: " + entity.name + "\t\t" + "Offset: " + str(entity.offset) + "\t\t" + "mode: " + str(entity.mode) + "\n"
            if (type(entity) == Function):
                result += "\tFunction: " + entity.name + "\t\t" + "Starting quad: " + str(entity.starting_quad) + "\t\t" + "Frame length:" + "\t" + str(entity.frame_length) + "\n"
                for formal in entity.formal_parameters :
                    result += "\t\tFormal Parameter: " + formal.name + "\t\t" + "mode: " + formal.mode + "\n"
            if (type(entity) == TemporaryVariable):
                result += "\tTemp Variable: " + entity.name + "\t\t" + "Offset: " + str(entity.offset) + "\n"
        
        return result

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
        global quadCounter
        if self.token.recognized_string in keyword :
            sys.exit("Invalid variable name inside function definition! \n Variable name shouldn't be a keyword!")
        
        if self.token.family == "Alphabetical" :
            global out_str
            main_name = self.token.recognized_string
            if len(self.symbol_table.scopes) == 0 :
                self.symbol_table.addScope()
            out_str += "\nCreated Scope: " + str(self.symbol_table.level) + "\t" + main_name + "\n"
            self.token = self.get_token()
            self.symbol_table.addEntityTable(main_name, "Function")
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
                            self.symbol_table.updateFields(ent_name= main_name, starting_quad = self.inter_code.nextQuad())
                            self.inter_code.genQuad("begin_block",main_name, "_","_")
                            self.statements()
                            if self.token.recognized_string == "#}" :
                                for entity in reversed(self.symbol_table.scopes[self.symbol_table.level].entities) :
                                    if (type(entity) != Function) :
                                        main_frame_length = entity.offset +  4
                                        break
                                self.symbol_table.updateFields(ent_name = main_name, frame_length = main_frame_length)
                                self.inter_code.genQuad("halt", "_", "_", "_")
                                self.inter_code.genQuad("end_block",main_name, "_","_")
                                self.createFinalCode(self.keep_line)
                                out_str += self.write_symbol_to_file(self.symbol_table.level)
                                out_str += "\nDeleted Scope: " + str(self.symbol_table.level) + " " + main_name + ". Function ended! \n"
                                
                                self.symbol_table.deleteScope(self.symbol_table.level)
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
        global func_name, out_str, func_name_list
        if self.token.recognized_string in keyword :
            sys.exit("Invalid variable name inside function definition! \n Variable name shouldn't be a keyword!")
        if self.token.family == "Alphabetical" :
            func_name = self.token.recognized_string 
            func_name_list.append(func_name)
            self.symbol_table.addEntityTable(func_name_list[self.func_numbers], "Function")
            self.symbol_table.addScope()
            out_str += "\nCreated Scope: " + str(self.symbol_table.level) + "\t" + func_name_list[self.func_numbers] + "\n"
            self.token = self.get_token()
            if self.token.recognized_string == "(" :
                self.token = self.get_token()
                self.idlist()
                global id_list_name
                result_list = id_list_name.split(",")
                for value in result_list :
                    self.symbol_table.addEntityTable(value, "Parameter")
                    self.symbol_table.updateFields(ent_name= value, offset= self.symbol_table.getCurrentScope().standard_offset)
                    self.symbol_table.getCurrentScope().standard_offset += 4
                    self.symbol_table.addFormalParameter(value)
                if self.token.recognized_string == ")" :
                    self.token = self.get_token()
                    if self.token.recognized_string == ":" :
                        self.token = self.get_token()
                        if self.token.recognized_string == "#{" :
                            self.token = self.get_token()
                            self.declarations()
                            while self.token.recognized_string == "def" :
                                self.func_numbers += 1
                                self.token = self.get_token()
                                self.def_function()
                            self.symbol_table.updateFields(ent_name = func_name_list[self.func_numbers], starting_quad = self.inter_code.nextQuad())
                            self.inter_code.genQuad("begin_block", func_name_list[self.func_numbers], "_","_")
                            self.statements()
                            if self.token.recognized_string == "#}" :
                                for entity in reversed(self.symbol_table.scopes[self.symbol_table.level].entities) :
                                    if (type(entity) != Function) :
                                        frame_length =  entity.offset + 4
                                        break
                                self.symbol_table.updateFields(ent_name = func_name_list[self.func_numbers], frame_length = frame_length)
                                self.inter_code.genQuad("end_block", func_name_list[self.func_numbers], "_","_") 
                                self.createFinalCode(self.keep_line)
                                out_str += self.write_symbol_to_file(self.symbol_table.level)
                                out_str += "\nDeleted Scope: " + str(self.symbol_table.level) + " " + func_name_list[self.func_numbers] + ". Function ended!\n"
                                self.symbol_table.deleteScope(self.symbol_table.level)
                                self.func_numbers -= 1
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
        global id_list_name, out_str
        if self.token.recognized_string == "#declare":
            self.token = self.get_token() 
            self.idlist()
            result_list = id_list_name.split(",")
            for value in result_list :
                self.symbol_table.addEntityTable(value, "Variable")
                self.symbol_table.updateFields(ent_name = value, offset = self.symbol_table.getCurrentScope().standard_offset)
                self.symbol_table.getCurrentScope().standard_offset += 4
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
        global out_str
        id = self.token.recognized_string
        name_list = []
        for ent in self.symbol_table.getCurrentScope().entities :
            name_list.append(ent.name)
        if id not in name_list:
            self.symbol_table.addEntityTable(id, "Variable")
            self.symbol_table.updateFields(ent_name = id, offset = self.symbol_table.getCurrentScope().standard_offset)
            self.symbol_table.getCurrentScope().standard_offset += 4
        self.token = self.get_token()
        if self.token.recognized_string == "=" :
            self.token = self.get_token()
            if self.token.recognized_string == "int" :
                self.token = self.get_token()
                if self.token.recognized_string == "(" :
                    self.token = self.get_token()
                    if self.token.recognized_string == "input" :
                        self.inter_code.genQuad("inp", "_", "_", id)
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
                self.inter_code.genQuad(":=", new_list[0], "_", id)
                self.token = self.get_token()
        else :
            sys.exit("Invalid simple statement syntax!")
        
    def print_stat(self) :
        global new_list
        self.token = self.get_token()
        if self.token.recognized_string == "(" :
            self.token = self.get_token()
            self.expression()
            if self.token.recognized_string == ")" :
                self.token = self.get_token()
                if self.token.recognized_string == ";" :
                    self.inter_code.genQuad("out", new_list[0], "_", "_")
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
                    self.inter_code.genQuad("retv", new_list[0], "_", "_")
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
            self.last_cond_quad = self.inter_code.quad_pointer.pointerHashMap[quadCounter]
            self.last_cond_quad.oper3 += 1
            self.inter_code.quad_pointer.pointerHashMap[quadCounter] = self.last_cond_quad
            if self.token.recognized_string == ")" :
                self.token = self.get_token()
                if self.token.recognized_string == ":" :
                    self.token = self.get_token()
                    if self.token.recognized_string == "#{" :
                        self.token = self.get_token()
                        if_false_list = self.inter_code.makeList(self.inter_code.nextQuad())
                        self.inter_code.genQuad("jump", "_", "_", "_")
                        self.statements()
                        if self.token.recognized_string == "#}" :
                            self.token = self.get_token()
                            if_true_list = self.inter_code.makeList(self.inter_code.nextQuad())
                            self.inter_code.genQuad("jump", "_", "_", "_")
                            self.inter_code.backPatch(if_false_list, self.inter_code.nextQuad())
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
                                    self.inter_code.backPatch(if_true_list, self.inter_code.nextQuad())
                                else :
                                    sys.exit("Invalid else syntax! \n ':' expected!")                                
                            else :
                                self.inter_code.backPatch(if_true_list, self.inter_code.nextQuad())
                        else :
                            sys.exit("Invalid if syntax! \n '#}' expected!")
                    else :
                        if_false_list = self.inter_code.makeList(self.inter_code.nextQuad())
                        self.inter_code.genQuad("jump", "_", "_", "_")
                        self.statement()
                        if_true_list = self.inter_code.makeList(self.inter_code.nextQuad())
                        self.inter_code.genQuad("jump", "_", "_", "_")
                        self.inter_code.backPatch(if_false_list, self.inter_code.nextQuad())
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
                        self.inter_code.backPatch(if_true_list, self.inter_code.nextQuad())
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
            whileQuad = quadCounter + 1
            self.condition()
            self.last_cond_quad = self.inter_code.quad_pointer.pointerHashMap[quadCounter]
            self.last_cond_quad.oper3 += 1
            self.inter_code.quad_pointer.pointerHashMap[quadCounter] = self.last_cond_quad
            while_false = self.inter_code.makeList(self.inter_code.nextQuad())
            self.inter_code.genQuad("jump", "_", "_", "_")
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
                    self.inter_code.genQuad("jump","_","_", whileQuad)
                    self.inter_code.backPatch(while_false, self.inter_code.nextQuad())
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
            global id_list_name 
            id_list_name = self.token.recognized_string
            self.token = self.get_token()
            while self.token.recognized_string == "," :
                id_list_name += self.token.recognized_string
                self.token = self.get_token()
                if self.token.recognized_string in keyword :
                    sys.exit("Invalid variable name in idlist syntax! \n Variable name should not be a keyword!")        
                if self.token.family == "Alphabetical" :
                    id_list_name += self.token.recognized_string
                    self.token = self.get_token()
                else :
                    sys.exit("Invalid kleene star in idlist syntax! \n ID expected after comma!")
        else :
            pass   

    def expression(self) :
        global new_list, quadCounter, out_str
        new_list = self.inter_code.emptyList()
        self.optional_sign()
        self.term()
        while self.token.family == "AddOper" : 
            operator = self.token.recognized_string
            self.token = self.get_token()
            self.term()
            w = self.inter_code.newTemp(IntermediateCode)
            self.symbol_table.addEntityTable(w, "TempVariable")
            self.symbol_table.updateFields(ent_name= w, offset= self.symbol_table.getCurrentScope().standard_offset)
            self.symbol_table.getCurrentScope().standard_offset += 4
            self.inter_code.genQuad(operator, new_list[0], new_list[-1], str(w))
            new_list[0] = w

    def term(self) :
        global out_str, new_list
        self.factor()
        while self.token.family == "MulOper" :
            operator = self.token.recognized_string
            self.token = self.get_token()
            self.factor()
            w = self.inter_code.newTemp(IntermediateCode)
            self.symbol_table.addEntityTable(w, "TempVariable")
            self.symbol_table.updateFields(ent_name= w, offset = self.symbol_table.getCurrentScope().standard_offset)
            self.symbol_table.getCurrentScope().standard_offset += 4
            self.inter_code.genQuad(operator, new_list[0], new_list[-1], str(w))
            new_list[0] = w

    def factor(self) :
        global new_list, id_name
        if self.token.family == "Number" :
            new_list.append(self.token.recognized_string)
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
            new_list.append(self.token.recognized_string)
            id_name = self.token.recognized_string
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
        global w, func_name, id_name, func_name_list
        called_func_name = ""
        if self.token.recognized_string == ")" :
            for my_name in func_name_list :
                if my_name == id_name :
                    called_func_name = id_name
                    break
            w = self.inter_code.newTemp(IntermediateCode)
            self.inter_code.genQuad("par", w, "RET", "_")
            self.inter_code.genQuad("call", "_", "_", called_func_name)
            new_list[0] = w
            self.symbol_table.addEntityTable(w, "TempVariable")
            self.symbol_table.updateFields(ent_name= w, offset = self.symbol_table.getCurrentScope().standard_offset)
            self.symbol_table.getCurrentScope().standard_offset += 4

        else :
            my_id = id_name
            self.expression()
            self.inter_code.genQuad("par", new_list[0], "CV", "_")
            while self.token.recognized_string == "," :
                self.token = self.get_token()
                self.expression()
                self.inter_code.genQuad("par", new_list[0], "CV", "_")

            w = self.inter_code.newTemp(IntermediateCode)
            self.inter_code.genQuad("par", w, "RET", "_")
            for my_name in func_name_list :
                if my_id == my_name  :
                    called_func_name = my_id
            
            self.inter_code.genQuad("call", "_", "_", called_func_name)
            new_list[0] = w
            self.symbol_table.addEntityTable(w, "TempVariable")
            self.symbol_table.updateFields(ent_name= w, offset = self.symbol_table.getCurrentScope().standard_offset)
            self.symbol_table.getCurrentScope().standard_offset += 4
          
    def optional_sign(self) :
        if self.token.family == "AddOper" :
            new_list.append(self.token.recognized_string)
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
            self.is_inverted = True
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
                operator = self.token.recognized_string 
                if self.is_inverted :
                    if operator == "<" :
                        operator = ">="
                    elif operator == ">" :
                        operator = "<="
                    elif operator == "<=" :
                        operator = ">"
                    elif operator == ">=" :
                        operator = "<"
                    elif operator == "!=" :
                        operator = "=="
                    elif operator == "==" :
                        operator = "!="
                first_new_list = new_list
                self.token = self.get_token() 
                self.expression()
                self.inter_code.genQuad(operator, first_new_list[0], new_list[0], quadCounter + 2)
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
                                            print("Compilation completed successfully!")
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
        global out_str
        if self.token.recognized_string == '(' :
            self.token = self.get_token()
            if self.token.recognized_string == ')' :
                self.token = self.get_token()
                if self.token.recognized_string == ';' :
                    self.token = self.get_token()
                    if self.token.recognized_string == "End Of File" :
                        for count, quad in self.inter_code.quad_pointer.pointerHashMap.items() :
                            self.output_code += self.write_quad_to_file(count , quad)
                        with open("intermediate_code.int", "w") as f , open("symbol_table.txt", "w") as g :
                            f.write(self.output_code)    
                            g.write(out_str)
                    else :
                        pass
                else :
                    sys.exit("Invalid syntax when calling main function! \n ';' expected!")
            else :
                sys.exit("Invalid syntax when calling main function! \n ')' expected!")
        else :
             sys.exit("Invalid syntax when calling main function! \n '(' expected!")

    def createFinalCode(self, start_index) :
        first_par = True
        d = 0
        if self.first_data_entry :
            self.final_code.produce(".data \nstr_nl: .asciz " + '"\\n"' + "\n.text\n\n\n")
            self.final_code.produce("L0: \n \tj Lmain\n")
            self.first_data_entry = False
        i = self.keep_line
        for i in range(start_index, len(self.inter_code.inter_code_list)) :
            self.keep_line = len(self.inter_code.inter_code_list) 
            if self.inter_code.inter_code_list[i].operator == "begin_block" :
                if "main_" in self.inter_code.inter_code_list[i].oper1 :
                    for scope in self.symbol_table.scopes :
                        for entity in scope.entities :
                            if entity.name == self.inter_code.inter_code_list[i].oper1 :
                                main_frame_length = entity.frame_length
                                self.final_code.produce("Lmain:\n")
                                self.final_code.produce("\taddi sp,sp,"+ str(main_frame_length) + "\n")
                                self.final_code.produce("\tmv s0,sp\n")
                                self.final_code.produce("\tsw ra,(sp)\n")
                else :
                    self.final_code.produce("L" + str((i + quad_length_list)) + ":\n")
                    self.final_code.produce("\tsw ra,(sp)\n")
            
            
            if self.inter_code.inter_code_list[i].operator == "+" or self.inter_code.inter_code_list[i].operator == "*" or self.inter_code.inter_code_list[i].operator == "//" or self.inter_code.inter_code_list[i].operator == "-" :
                self.final_code.produce("L" + str((i + quad_length_list)) + ":\n")
                self.final_code.loadvr(self.inter_code.inter_code_list[i].oper1, "t1")
                self.final_code.loadvr(self.inter_code.inter_code_list[i].oper2, "t2")
                
                if self.inter_code.inter_code_list[i].operator == "+" :
                    oper = "add"
                elif self.inter_code.inter_code_list[i].operator == "*" :
                    oper = "mul"
                elif self.inter_code.inter_code_list[i].operator == "//" :
                    oper = "div"
                else :
                    oper = "sub"
                self.final_code.produce("\t" + oper + " t1,t1,t2\n")
                self.final_code.storerv("t1" ,self.inter_code.inter_code_list[i].oper3) 

            if self.inter_code.inter_code_list[i].operator == "<" or self.inter_code.inter_code_list[i].operator == ">" or self.inter_code.inter_code_list[i].operator == "<=" or self.inter_code.inter_code_list[i].operator == ">=" or self.inter_code.inter_code_list[i].operator == "==" or self.inter_code.inter_code_list[i].operator == "!=" :
                self.final_code.produce("L" + str((i + quad_length_list)) + ":\n")
                self.final_code.loadvr(self.inter_code.inter_code_list[i].oper1, "t1")
                self.final_code.loadvr(self.inter_code.inter_code_list[i].oper2, "t2")
                oper = ""
                if self.inter_code.inter_code_list[i].operator == ">" :
                    oper = "bgt"
                elif self.inter_code.inter_code_list[i].operator == "<" :
                    oper = "blt"
                elif self.inter_code.inter_code_list[i].operator == ">=" :
                    oper = "bge"
                elif self.inter_code.inter_code_list[i].operator == "<=" :
                    oper = "ble"
                elif self.inter_code.inter_code_list[i].operator == "==" :
                    oper = "beq"
                else :
                    oper = "bne"
                self.final_code.produce("\t" + oper + " t1,t2,L" + str(self.inter_code.inter_code_list[i].oper3) + "\n")
                
            if self.inter_code.inter_code_list[i].operator == ":=" :
                self.final_code.produce("L" + str((i + quad_length_list)) + ":\n")
                self.final_code.loadvr(self.inter_code.inter_code_list[i].oper1, "t1")
                self.final_code.storerv("t1", self.inter_code.inter_code_list[i].oper3)
            
            if self.inter_code.inter_code_list[i].operator == "retv" :
                self.final_code.produce("L" + str((i + quad_length_list)) + ":\n")
                self.final_code.produce("\tlw t0, -8(sp)\n")
                self.final_code.loadvr(self.inter_code.inter_code_list[i].oper1, "t1")
                self.final_code.produce("\tsw t1, (t0)\n")
                self.final_code.produce("\tlw ra,(sp)\n\tjr ra\n")           


            if self.inter_code.inter_code_list[i].operator == "end_block" : 
                self.final_code.produce("L" + str((i + quad_length_list)) + ":\n")
                self.final_code.produce("\tlw ra,(sp)\n\tjr ra\n")           
            
            if self.inter_code.inter_code_list[i].operator == "out" :
                self.final_code.produce("L" + str((i + quad_length_list)) + ":\n")
                self.final_code.loadvr(self.inter_code.inter_code_list[i].oper1, "a0")
                self.final_code.produce("\tli a7,1\n")
                self.final_code.produce("\tecall\n")
                self.final_code.produce("\tla a0,str_nl\n")
                self.final_code.produce("\tli a7,4\n")
                self.final_code.produce("\tecall\n")

        
            if self.inter_code.inter_code_list[i].operator == "inp" :
                self.final_code.produce("L" + str((i + quad_length_list)) + ":\n")
                self.final_code.produce("\tli a7,5\n")
                self.final_code.produce("\tecall\n")
                self.final_code.storerv("a0", self.inter_code.inter_code_list[i].oper3)
            
            if self.inter_code.inter_code_list[i].operator == "halt" :
                self.final_code.produce("L" + str((i + quad_length_list)) + ":\n")
                self.final_code.produce("\tli a0,0\n")
                self.final_code.produce("\tli a7,93\n")
                self.final_code.produce("\tecall\n")

            if self.inter_code.inter_code_list[i].operator == "par" :
                self.final_code.produce("L" + str((i + quad_length_list)) + ":\n")
                if self.inter_code.inter_code_list[i].oper2 == "CV" :
                    if first_par :
                        for quad in self.inter_code.inter_code_list :
                            if quad.operator == "call" :
                                the_called_func_name = quad.oper3
                                for scope in self.symbol_table.scopes :
                                    for entity in scope.entities :
                                        if the_called_func_name == entity.name :
                                            frame_length = entity.frame_length
                                            self.final_code.produce("\taddi fp,sp," + str(frame_length) + "\n")
                                            first_par = False
                                            break        
                                break
                    self.final_code.loadvr(self.inter_code.inter_code_list[i].oper1, "t1")
                    self.final_code.produce("\tsw t1,-" + str((12+4*d))+"(fp)\n")
                    d += 1
                if self.inter_code.inter_code_list[i].oper2 == "RET" :
                    result = self.symbol_table.searchForEntry(self.inter_code.inter_code_list[i].oper1)
                    entity = result[0]
                    offset = entity.offset
                    self.final_code.produce("\taddi t0,sp,-" + str(offset) + "\n")
                    self.final_code.produce("\tsw t0,-8(fp)\n")

            if self.inter_code.inter_code_list[i].operator == "call" :
                self.final_code.produce("L" + str((i + quad_length_list)) + ":\n")
                name = self.inter_code.inter_code_list[i].oper3
                for scope in self.symbol_table.scopes :
                    for entity in scope.entities :
                        if entity.name == name :
                            frame_length = entity.frame_length
                            starting_quad = entity.starting_quad
                            break
                result = self.symbol_table.searchForEntry(name)
                func_level = result[1]
                my_level = self.symbol_table.getCurrentScope().level
                if my_level == func_level :
                    self.final_code.produce("\tlw t0,-4(sp)\n")
                    self.final_code.produce("\tsw t0-4(fp)\n")
                else : 
                    self.final_code.produce("\tsw sp,-4(fp)\n")
                self.final_code.produce("\taddi sp,sp," + str(frame_length) + "\n")
                self.final_code.produce("\tjal L" + str(starting_quad) + "\n")
                self.final_code.produce("\taddi sp,sp,-" + str(frame_length) + "\n")

            if self.inter_code.inter_code_list[i].operator == "jump" :
                self.final_code.produce("L" + str((i + quad_length_list)) + ":\n")
                self.final_code.produce("\tj L" + str(self.inter_code.inter_code_list[i].oper3) + "\n")

        
if __name__ == '__main__' :
    if len(sys.argv) < 2 :
        sys.exit("The format is 'python 'cutepy_4761_4765'.py 'test_file'.cpy !'")

    input_file = sys.argv[1]
    my_lex = Lex(input_file,1)
    my_parser = Syntax_Analyzer(input_file, my_lex)
    my_parser.start_rule()
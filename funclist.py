import collections

FuncList = collections.namedtuple("FuncList", ['head', 'tail'])


def all_values_above(funclist, threshold):
    """ @return a funclist containing all the items from funclist greater than threshold """
    pass


def only_values_matching(funclist, tester):
    """ 
    @param tester: a boolean function for testing items from a funclist
    @return a funclist containing all the items from funclist on which the tester function returns True
    """
    pass


def mult_all(funclist, multiplier):
    if funclist:
        return FuncList(funclist.head*multiplier, mult_all(funclist.tail, multiplier))
    else:
        return None


def apply_to_all(funclist, function_to_call):
    if funclist:
        return FuncList(function_to_call(funclist.head), apply_to_all(funclist.tail, function_to_call))
    else:
        return None












def convert_to_funclist(reglist):
    if reglist:
        return(FuncList(reglist[0], convert_to_funclist(reglist[1:])))
    else:
        return None
        

def convert_to_reglist(funclist):
    if funclist == None:
       return []
    else:
       reglist = convert_to_reglist(funclist.tail)
       reglist.insert(0, funclist.head)
       return reglist
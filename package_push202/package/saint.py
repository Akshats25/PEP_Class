def help_menu():
    """
    This is a module which has three functions. 
    
    help_menu : this function to know what does the module contains and it's funtionality.
    remove_char : this function can be used to remove a charecter from a given string or expression.
    remove_html_char : this function helps to remove the brackets and slash in html code.
    """
    print(help_menu.__doc__)

def remove_char(s,a):
    while a in s:
        s = s.replace(a,"")
    return s
def remove_html_char(a):
    while((">" in a) | ("<" in a) | ("/" in a)):
        a = a.replace(">", "")
        a = a.replace("<", "")
        a = a.replace("/", "")
    return a

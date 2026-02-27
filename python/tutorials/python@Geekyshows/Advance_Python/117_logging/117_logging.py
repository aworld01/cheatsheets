"""
Logging is useful to track the error or exception or information. It also helps in debugging.

basicConfig(**kwargs): This method is used to config the logging System.
Syntax:-
    basicConfig(**kwargs)

filename: It specifies that a FileHandler be created, using the specified filename, rather than a StreamHandler.
filemode: If filename is specified, open the file in this mode. Default to 'a'. We can write 'w'
level: Set the root logger level to the specified level.

format: Use the specified format string for the handler.

datefmt: Use the specified date/time format, as accepted by time.strftime().

style: If format is specified, use this style for the format string. One of "%" "{" or "$" for print-style, str.format() or string. Template respectively. Defaults to "%".




This method is used to config the logging System.

stream: Use the specified stream to initialize the StreamHandler. Note that this argument is incompatible with filename - if both are present, a ValueError is raised.

handlers: If specified, this should be an iterable of already created handlers to add the root logger. Any handlers which dont't already have a formatter set will be assigned the default formatter created in this function. Note that this argument is incompatible with filename or stream - if both are present, a ValueError is raised.

force: If this keyword argumaent is specified as true, any existing handlers attached to the root logger are removed and closed, before carrying out the configuration as specified by the other arguments.


METHODS
getLogger(): This method returns a logger with the specified name or, if name is None, return a logger which is the root logger of the hierarchy, If specified, the name is typically a dot-separated hierarchical name like "a", "a.b" or "a.b.c.d".

info(msg): This will log a message with level INFO on this logger.
warning(msg): This will log a message with level WARNING on this logger.
error(msg): This will log a message with level ERROR on this logger.
critical(msg): This will log a message with level CRITICAL on this logger.
exception(msg): This will log a message with level ERROR on this logger.

FORMAT
Format can take a string with LogRecord attributes in any arrangement you like.

asctime: Human-readable time when the LogRecord was created. By default this is of the from "2003-07-08 16-:49:45,896" (the numbers after the comma are millisecond portion of the time).
Ex:-
    %(asctime)s

created: Time when the LogRecord was created (as returned by time.time())
Ex:-
    %(filename)s



LogRecord Attributes
levelname: Text logging level for the message('DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL').
Ex:-
    %(levelno)s

lineno: Source line number where the logging call was issued (if available).
Ex:-
    %(lineno)d

message: The logged message, computed as msg % args. This is set when Formatter.format() is invoked.
Ex:-
    %(message)s

name: Name of the logger used to log the call.
Ex:-
    %(name)s

pathname: Full pathname of the source file where the logging call was issued (if available).
Ex:-
    %(pathname)s

args
exc_info
funcname
module
msecs
msg
process
processname
relativecreated
stack_info
thread
threadname
"""
from logging import*

"""we can see only high_level loggings"""
# warning("This is warning")
# error("This is Error")
# critical("This is Critical")
# debug("This is debug") #this will be not displayed because of low_level



"""to save into file"""
# basicConfig(filename="logFile.log") #to create a log file (default mode is "Append")

# warning("This is warning")
# error("This is Error")
# critical("This is Critical")
# debug("This is Debug")


"""to set level"""
# basicConfig(filename="logFile.log", level=DEBUG) #to set level

# warning("This is warning")
# error("This is Error")
# critical("This is Critical")
# debug("This is Debug")
# info("This is Info")


"""to change mode"""
# basicConfig(filename="logFile.log", level=DEBUG, filemode="w") #to change filemode

# warning("This is warning in 'w' mode")
# error("This is Error")
# critical("This is Critical")



"""to format message"""
# basicConfig(filename="logFile.log", level=DEBUG, filemode="w", format="%(asctime)s: %(message)s") #to format the message

# warning("This is warning")
# error("This is Error")
# critical("This is Critical")


# log_format = "%(asctime)s: %(message)s"
# basicConfig(filename="logFile.log", level=DEBUG, filemode="w", format=log_format) #to format the message

# warning("This is warning")
# error("This is Error")
# critical("This is Critical")



"""to format message with line_number"""
# log_format = "%(lineno)d - %(asctime)s: %(message)s"
# basicConfig(filename="logFile.log", level=DEBUG, filemode="w", format=log_format) #to format the message

# warning("This is warning")
# error("This is Error")
# critical("This is Critical")



# """format message with '{'"""
# log_format = "{lineno} - {asctime} {name}: {message}"
# basicConfig(filename="logFile.log", level=DEBUG, filemode="w", format=log_format,  style='{') #to format the message

# warning("This is warning")
# error("This is Error")
# critical("This is Critical")



"""change user"""
logger = getLogger("Geek") #to set user

log_format = "{lineno} - {asctime} {name}: {message}"
basicConfig(filename="logFile.log", level=DEBUG, filemode="w", format=log_format,  style='{') #to format the message

logger.warning("This is warning")
logger.error("This is Error")
logger.critical("This is Critical")
# Stage 1 – Professional Python Syllabus

Goal: Become internship-ready in Python engineering.
Estimated Outcome:
* Build production-quality Python code.
* Pass Python interview rounds.
* Build backend projects confidently.

---

### Competency 1.1: Python Data Model

* **Why Learn It?**: Understanding how Python manages objects, variables, and memory under the hood is critical for writing memory-efficient, bug-free applications.
* **Industry Usage**: Crucial for custom container classes, debugging memory leaks, optimizing large-scale data processing pipelines, and writing custom libraries.
* **AI Usage**: AI assistants can write syntactically correct Python, but often generate subtle bugs related to mutable default arguments or incorrect identity vs equality checks. Developers need this competency to debug and audit AI-generated code.
* **Prerequisites**: Basic knowledge of variables, assignments, and fundamental types (lists, integers, strings).
* **Exact Topics**:
  - Variables as references (pointers to objects)
  - Identity vs. Equality (`is` vs `==`)
  - Mutability (mutable vs. immutable types)
  - Object lifecycle and Garbage Collection (reference counting, cyclic references)
  - Shallow vs. Deep copying (`copy.copy` vs `copy.deepcopy`)
  - Integer caching/interning and string interning (e.g., `-5` to `256` behavior)
* **Best Resources**:
  - *Fluent Python (2nd Edition)* - Chapter 1 & Chapter 6 (Object References, Mutability, and Recycling)
  - Corey Schafer - Python Tutorial: Mutability and `is` vs `==`
* **Official Documentation**:
  - [Python Data Model](https://docs.python.org/3/reference/datamodel.html)
  - [copy module](https://docs.python.org/3/library/copy.html)
* **Practice Exercises**:
  - Write a script that checks if two variables refer to the same object or different objects with the same value under various scenarios (int, list, string).
  - Create a custom class and verify how it behaves with `copy` and `deepcopy`.
* **Mini Project**:
  - **Object Inspector CLI**: A tool that accepts any Python object, analyzes it dynamically, and prints out its memory address (hex), reference count (using `sys.getrefcount`), mutability, and a map of its internal attributes.
* **Common Mistakes**:
  - Using mutable default arguments in functions (e.g., `def append_to(element, target=[]):`).
  - Confusing `is` and `==` (using `is` for value comparison).
  - Modifying a list or dict while iterating over it.
* **Interview Questions**:
  - What is the difference between `is` and `==` in Python?
  - Explain the behavior and fix for: `def func(val, data=[]): data.append(val); return data`.
  - How does Python's Garbage Collection work, and what is a cyclic reference?
* **Exit Criteria**:
  - You can explain why `[]` is evaluated dynamically and how to use `None` as a sentinel default.
  - You can correctly identify when to use `copy.deepcopy` instead of a shallow copy.
* **Code Review Checklist**:
  - No mutable default arguments.
  - Correct use of `is None` for sentinel checks.
  - Proper handling of object copies to avoid unintended side effects.

---

### Competency 1.2: Functions

* **Why Learn It?**: Functions are the primary building blocks of code. Mastering parameter types, scopes, and functional programming concepts enables writing clean, modular, and reusable code.
* **Industry Usage**: API design, CLI interfaces, event handlers, callback registers, and standard library wrapper utilities.
* **AI Usage**: Modern AI tools generate functional code easily, but often miss type hints, use incorrect parameter combinations (e.g. not using keyword-only arguments to protect API changes), or overuse slow lambda expressions.
* **Prerequisites**: Competency 1.1 (Data Model).
* **Exact Topics**:
  - Positional-only (`/`) and Keyword-only (`*`) parameters
  - Variadic arguments (`*args` and `**kwargs`)
  - Argument unpacking
  - First-class functions (passing functions as arguments, returning functions)
  - Lambdas and anonymous functions
* **Best Resources**:
  - *Fluent Python* - Chapter 7 (Functions as First-Class Objects)
  - Corey Schafer - Python Tutorial: Functions
* **Official Documentation**:
  - [Defining Functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
* **Practice Exercises**:
  - Write a function that enforces positional-only arguments for two inputs, keyword-only for two others, and accepts arbitrary extra arguments.
  - Implement a basic map/filter utility using lambdas and first-class functions.
* **Mini Project**:
  - **Command Router / Dispatcher CLI**: A CLI application that registers functions to specific string commands (e.g., `add`, `subtract`) dynamically and invokes them with user-supplied arguments via `*args` and `**kwargs`.
* **Common Mistakes**:
  - Overusing lambda functions where standard named functions are cleaner and easier to debug.
  - Mixing up argument ordering (`def func(*args, positional, **kwargs)`).
  - Mutating mutable arguments passed to functions.
* **Interview Questions**:
  - What are positional-only and keyword-only arguments, and why would you use them?
  - Explain how `*args` and `**kwargs` unpack parameters under the hood.
* **Exit Criteria**:
  - You can design an API that prevents users from passing positional arguments for configuration parameters.
  - You can explain the difference between a function reference and a function call.
* **Code Review Checklist**:
  - Functions are small, cohesive, and have a single responsibility.
  - API parameters are properly constrained with `/` and `*` where appropriate.
  - Clear and descriptive docstrings and parameter names.

---

### Competency 1.3: Scope & Closures

* **Why Learn It?**: Understanding scopes prevents variable shadow bugs and is the prerequisite for decorators, stateful functions without classes, and advanced design patterns.
* **Industry Usage**: Implementing decorators, caching mechanisms, callback factories, and event-driven architecture.
* **AI Usage**: Code completion tools can easily confuse local scopes with parent scopes or generate bugs when using `global` or `nonlocal` keywords improperly.
* **Prerequisites**: Competency 1.2 (Functions).
* **Exact Topics**:
  - LEGB Rule (Local, Enclosing, Global, Built-in)
  - Variable shadowing
  - `global` and `nonlocal` keywords
  - Closures (preserving outer function state)
  - Cell objects and the `__closure__` attribute
* **Best Resources**:
  - Real Python - Python Scope & LEGB Rule
  - *Fluent Python* - Chapter 9 (Decorators and Closures - Closure section)
* **Official Documentation**:
  - [Python Scopes and Namespaces](https://docs.python.org/3/tutorial/classes.html#python-scopes-and-namespaces)
* **Practice Exercises**:
  - Create a nested function structure and modify a variable in the enclosing scope using `nonlocal`.
  - Inspect the `__closure__` attribute of a returned function to see the cell objects holding state.
* **Mini Project**:
  - **Stateful Counter & Auth Factory**: Implement a stateful configuration manager/counter that stores keys, configurations, or call history in closures, acting as a lightweight, class-free state machine.
* **Common Mistakes**:
  - Using `global` to modify global variables instead of passing arguments/returning values.
  - `UnboundLocalError`: trying to assign a local variable before declaring it, shadowing an enclosing variable.
* **Interview Questions**:
  - What is a closure in Python, and how does it retain access to enclosing variables?
  - Explain the difference between `global` and `nonlocal` keywords.
* **Exit Criteria**:
  - You can write a stateful closure that tracks its own execution count without global variables or class properties.
  - You can explain how the `__closure__` tuple maps variables to cells.
* **Code Review Checklist**:
  - No unnecessary use of the `global` keyword.
  - Enclosing scopes are kept small to prevent memory leaks in closures.

---

### Competency 1.4: Object-Oriented Programming (OOP)

* **Why Learn It?**: OOP is the paradigm for structuring complex enterprise applications. Understanding OOP concepts ensures maintainable, reusable, and extendable code.
* **Industry Usage**: Model layer in web frameworks (Django, SQLAlchemy), building SDKs, game development, GUI frameworks, and domain-driven design.
* **AI Usage**: AI models often generate bloated class structures or miss crucial pythonic design patterns, such as using `@property` or implementing magic methods correctly.
* **Prerequisites**: Competencies 1.1 to 1.3.
* **Exact Topics**:
  - Classes, instances, and the `__init__` constructor
  - Instance, class (`@classmethod`), and static (`@staticmethod`) methods
  - Encapsulation, private/protected access modifiers (name mangling `__variable`)
  - Properties (`@property`, setters, deleters)
  - Inheritance, Method Resolution Order (MRO), and `super()`
  - Composition vs. Inheritance
  - Magic (dunder) methods (`__str__`, `__repr__`, `__len__`, `__getitem__`, etc.)
  - Basic SOLID Principles
* **Best Resources**:
  - Corey Schafer - Object-Oriented Programming Series (6 Videos)
  - *Fluent Python* - Chapter 11 through 14 (Object-Oriented Idioms)
* **Official Documentation**:
  - [Classes](https://docs.python.org/3/tutorial/classes.html)
* **Practice Exercises**:
  - Create a class hierarchy demonstrating MRO and how `super()` resolves in multiple inheritance.
  - Implement a class with read-only properties and validate modifications through a setter property.
* **Mini Project**:
  - **Inventory Management System**: Design a modular inventory system using OOP. Implement custom collections using magic methods to allow indexing, length checks, and readable representations. Apply polymorphism and composition to handle different product types and discount structures.
* **Common Mistakes**:
  - Overusing inheritance instead of composition.
  - Using `@classmethod` when the method doesn't need access to the class namespace.
  - Failing to implement `__repr__` for custom debugging output.
* **Interview Questions**:
  - What is the difference between `@classmethod` and `@staticmethod`?
  - How does Python's Method Resolution Order (MRO) work, especially with multiple inheritance (Diamond problem)?
  - How do you implement a read-only property in a Python class?
* **Exit Criteria**:
  - You can explain and implement the difference between `__str__` and `__repr__`.
  - You can construct a multiple-inheritance model and map the output of `Class.__mro__`.
* **Code Review Checklist**:
  - Composition is preferred over deep inheritance trees.
  - Property decorators are used instead of getter/setter methods (e.g. `get_value()`, `set_value()`).
  - Class variables are not accidentally shadowed by instance assignments.

---

### Competency 1.5: Exception Handling

* **Why Learn It?**: Unhandled exceptions crash programs. Proper error handling makes applications resilient, secure, and user-friendly.
* **Industry Usage**: API error responses, database transaction rollbacks, file I/O operations, network request retries, and system recovery.
* **AI Usage**: AI code suggestions frequently overuse bare `except:` clauses or mask errors by suppressing tracebacks, which creates severe stability and debugging hazards in production.
* **Prerequisites**: Competencies 1.1 to 1.4.
* **Exact Topics**:
  - `try`, `except`, `else`, `finally` control blocks
  - Exception hierarchy and catching specific exceptions
  - Raising exceptions and exception chaining (`raise ... from ...`)
  - Custom exceptions (inheriting from `Exception`)
  - Contextual error information (tracebacks, sys.exc_info)
* **Best Resources**:
  - Corey Schafer - Python Tutorial: Try/Except Blocks for Handling Errors
  - Real Python - Python Exceptions: An Introduction
* **Official Documentation**:
  - [Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html)
  - [Built-in Exceptions](https://docs.python.org/3/library/exceptions.html)
* **Practice Exercises**:
  - Create a division calculator that catches `ZeroDivisionError` and `ValueError`, implementing a `finally` block to close a simulated database logging resource.
  - Write a custom exception containing error codes and metadata, raising it with explanation.
* **Mini Project**:
  - **Robust Banking System Simulation**: Create a backend module for accounts. Raise custom exceptions like `InsufficientFundsError` and `InvalidTransactionError`. Use exception chaining to capture root causes, and log transaction logs inside a `finally` block to guarantee audit records.
* **Common Mistakes**:
  - Catching all exceptions with a bare `except:` block (which intercepts `KeyboardInterrupt` and `SystemExit`).
  - Catching `BaseException` instead of `Exception`.
  - Swallowing exceptions silently (ignoring error states).
* **Interview Questions**:
  - Why is using a bare `except:` bad practice?
  - What is the purpose of the `else` block in a `try/except` statement?
  - Explain the difference between `raise Exception` and `raise Exception from e`.
* **Exit Criteria**:
  - You can write structured error-handling code that guarantees external resource cleanup.
  - You can trace how custom exceptions pass up the call stack.
* **Code Review Checklist**:
  - No bare `except:` statements.
  - Clean error propagation and descriptive error messages.
  - Resources are properly released under all failure paths.

---

### Competency 1.6: File Handling

* **Why Learn It?**: Applications regularly interact with files. Efficient, cross-platform, and secure file operations prevent file locks, corruption, and resource leakage.
* **Industry Usage**: Parsing config files (JSON, YAML), processing logs, processing CSV reports, exporting data, and handling uploads.
* **AI Usage**: AI code generation often relies on older `os.path` operations rather than modern `pathlib`, or forgets to use context managers, leading to file handle leaks.
* **Prerequisites**: Competency 1.5 (Exception Handling).
* **Exact Topics**:
  - File reading and writing modes (`r`, `w`, `a`, `x`, `b`)
  - Context managers (`with` statement) for automatic closing
  - Modern path operations with `pathlib`
  - Reading/writing structured formats: JSON and CSV
  - Buffer management and encoding configurations (UTF-8)
* **Best Resources**:
  - Corey Schafer - Python Tutorial: File Objects - Reading and Writing to Files
  - Real Python - Python's pathlib Module: Taming the File System
* **Official Documentation**:
  - [Reading and Writing Files](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
  - [pathlib module](https://docs.python.org/3/library/pathlib.html)
* **Practice Exercises**:
  - Write a script that checks if a file path exists using `pathlib`, reads its content, reverses it, and writes to a new destination.
  - Parse a JSON file containing user objects, append a new user, and save it back without corrupting the file.
* **Mini Project**:
  - **Dynamic Log Analyzer**: Write a script that reads a large log file line-by-line using context managers, extracts error statistics using CSV format, outputs a summarized JSON report, and archives processed logs to a backup folder using `pathlib`.
* **Common Mistakes**:
  - Opening files without `with` context managers (forgetting to call `.close()`).
  - Hardcoding path separators (e.g., `folder\file.txt` or `folder/file.txt`) instead of using `pathlib.Path`.
  - Omitting the `encoding="utf-8"` parameter, causing errors when code runs on different OS defaults.
* **Interview Questions**:
  - Why is it preferred to use `pathlib.Path` over `os.path`?
  - How do you ensure files are closed even if an exception occurs during execution?
  - What happens if you try to open a file in write mode (`w`) vs append mode (`a`)?
* **Exit Criteria**:
  - You can write a cross-platform file operation tool that handles unicode characters safely.
  - You can parse CSV/JSON data structures using Python's standard library.
* **Code Review Checklist**:
  - Context managers (`with`) are used for all file access.
  - `pathlib.Path` is used instead of `os` or string concatenation for path manipulation.
  - Explicit file encoding (`encoding="utf-8"`) is always declared.

---

### Competency 1.7: Logging

* **Why Learn It?**: Real-world applications run on headless servers where `print()` statements are useless. Logging provides structured, persistent diagnostic trails.
* **Industry Usage**: Production system monitoring, audit logs, error reporting, performance monitoring, and compliance logs.
* **AI Usage**: AI systems don't have human runtime context and heavily rely on structured log outputs to debug production issues. Writing good log instrumentation is vital for AI-assisted debugging.
* **Prerequisites**: Competencies 1.5 and 1.6.
* **Exact Topics**:
  - Why `print()` is an anti-pattern in production
  - Logger objects and hierarchy
  - Log levels: DEBUG, INFO, WARNING, ERROR, CRITICAL
  - Formatters, Handlers (StreamHandler, FileHandler)
  - Log rotation (RotatingFileHandler, TimedRotatingFileHandler)
  - Configuration via dictionary and code
* **Best Resources**:
  - Corey Schafer - Python Tutorial: Logging Basics & Advanced
  - Real Python - Logging in Python
* **Official Documentation**:
  - [Logging HOWTO](https://docs.python.org/3/howto/logging.html)
  - [logging module](https://docs.python.org/3/library/logging.html)
* **Practice Exercises**:
  - Set up a logger that outputs INFO-level logs to the console and ERROR-level logs to a file.
  - Implement log rotation to limit log sizes to 10KB, keeping up to 3 backup files.
* **Mini Project**:
  - **Refactored Codebase with Logging System**: Revisit the Banking System (from Competency 1.5) and completely replace all terminal `print()` statements with structured logs. Route standard info logs to `console` and transactional logs with context to a rotated `audit.log` file.
* **Common Mistakes**:
  - Using string formatting inside logging calls (e.g. `logging.info(f"User {u} logged in")` instead of lazy evaluation: `logging.info("User %s logged in", u)`).
  - Mixing standard print output with logging output.
  - Hardcoding logging configuration in child packages instead of configuring it at the entrypoint.
* **Interview Questions**:
  - Why should we use logging lazy evaluation (`logger.debug("Val: %s", val)`) instead of f-strings?
  - What are the main components of Python's logging architecture?
* **Exit Criteria**:
  - You can explain how log messages bubble up the logger tree.
  - You can configure log output formatting including timestamps, line numbers, and levels.
* **Code Review Checklist**:
  - Zero `print()` statements in package files.
  - Correct use of log levels (e.g., info vs. debug vs. error).
  - No f-strings inside log parameters where lazy evaluation is preferred.

---

### Competency 1.8: Decorators

* **Why Learn It?**: Decorators let you modify the behavior of functions or classes cleanly, adhering to the DRY (Don't Repeat Yourself) principle and promoting code reuse.
* **Industry Usage**: Route definition (Flask/FastAPI), authentication/authorization, transaction management, rate limiting, and execution caching (memoization).
* **AI Usage**: Code assistants are great at applying decorators, but frequently introduce issues with variable scope inside closures or fail to preserve function metadata, breaking introspective tools.
* **Prerequisites**: Competency 1.3 (Scope & Closures).
* **Exact Topics**:
  - Inner and outer functions (wrappers)
  - Passing arguments to decorated functions
  - Preserving function identity with `functools.wraps`
  - Decorators that accept custom configuration arguments
  - Class decorators and stacking multiple decorators
* **Best Resources**:
  - Corey Schafer - Python Tutorial: Decorators - Dynamically Alter the Behavior of Functions
  - *Fluent Python* - Chapter 9 (Decorators and Closures)
* **Official Documentation**:
  - [functools module](https://docs.python.org/3/library/functools.html)
* **Practice Exercises**:
  - Implement a decorator `log_calls` that prints function arguments and return values when a function is called.
  - Write a decorator that retries a function three times with a brief delay before raising an error.
* **Mini Project**:
  - **API Rate Limiter & Auth Decorator Suite**: Build a set of decorators for API handlers. Implement `@require_role("admin")` to intercept and check simulated request permissions, `@rate_limit(max_calls=5)` to throttle execution, and `@execution_timer` to measure microsecond latency.
* **Common Mistakes**:
  - Forgetting to use `@functools.wraps`, causing functions to lose their name (`__name__`) and docstring (`__doc__`).
  - Misunderstanding execution order (decorators are evaluated at import time, wrappers run at invocation time).
* **Interview Questions**:
  - Why do we use `@wraps` from `functools` when creating custom decorators?
  - How do you write a decorator that accepts its own runtime arguments (e.g. `@retry(attempts=3)`)?
* **Exit Criteria**:
  - You can write a parameterized decorator that maintains correct wrapper function signatures.
  - You can explain the difference between decorator load-time and runtime execution.
* **Code Review Checklist**:
  - Every decorator uses `@functools.wraps`.
  - Stacked decorators are ordered logically.

---

### Competency 1.9: Generators

* **Why Learn It?**: When processing large datasets, loading everything into memory crashes systems. Generators allow processing data streams incrementally with minimal memory.
* **Industry Usage**: Large CSV/log processors, database cursor streams, web scraping pipelines, and custom event loops.
* **AI Usage**: AI systems frequently write standard list-building structures that cause Out-Of-Memory (OOM) errors in production. Developers must know how to restructure these into generators.
* **Prerequisites**: Competencies 1.1 and 1.6.
* **Exact Topics**:
  - The `yield` keyword vs `return`
  - The Iterator Protocol (`__next__` and `__iter__`)
  - Generator expressions
  - Infinite sequences and lazy evaluation
  - Memory consumption profiling (`sys.getsizeof`)
  - Advanced generator controls (sending values with `.send()`, `.throw()`, `.close()`)
* **Best Resources**:
  - Corey Schafer - Python Tutorial: Generators - How to use them and the benefits
  - *Fluent Python* - Chapter 17 (Iterators, Generators, and Classic Coroutines)
* **Official Documentation**:
  - [Generators](https://docs.python.org/3/howto/functional.html#generators)
  - [Generator Expressions](https://docs.python.org/3/reference/expressions.html#generator-expressions)
* **Practice Exercises**:
  - Write a generator that yields Fibonacci  numbers up to a specified ceiling.
  - Compare the memory usage of a list comprehension vs a generator expression for 1 million integers using `sys.getsizeof`.
* **Mini Project**:
  - **Large CSV Stream Processor**: Build a parser that streams a massive CSV dataset (e.g., 500MB+ logs or transactions) line-by-line without loading the file into memory. Filter, transform, and map entries into database records iteratively, verifying low memory overhead during operation.
* **Common Mistakes**:
  - Attempting to index or slice a generator directly (`gen[0]`), which causes a TypeError.
  - Trying to reuse a generator after it has completed execution (generators are one-shot streams).
* **Interview Questions**:
  - What is the difference between a generator and a standard function?
  - How does Python's iterator protocol work under the hood?
  - What is the difference in memory profile between `[x for x in range(1000000)]` and `(x for x in range(1000000))`?
* **Exit Criteria**:
  - You can convert memory-heavy list processing code to memory-efficient generator code.
  - You can explain and debug the `StopIteration` exception.
* **Code Review Checklist**:
  - Infinite loops/iterators are handled safely without freezing threads.
  - Generator expressions are used to process sequences lazily where intermediate lists are not needed.

---

### Competency 1.10: Context Managers

* **Why Learn It?**: Ensures resources are always cleanly closed, committed, or rolled back, protecting databases and OS systems from locks and leaks.
* **Industry Usage**: Database transaction boundaries, file and stream operations, thread locks, network sockets, mock testing, and temporary environmental configuration.
* **AI Usage**: AI assistants routinely construct context managers but might fail to handle nested resource management cleanly, requiring developers to audit context layouts.
* **Prerequisites**: Competencies 1.4 and 1.5.
* **Exact Topics**:
  - The `with` statement and resource lifecycle
  - Class-based context managers: `__enter__` and `__exit__`
  - Handling exceptions inside `__exit__` (suppress vs propagate)
  - Function-based context managers: `@contextmanager` from `contextlib`
  - Nested context managers and `ExitStack`
* **Best Resources**:
  - Real Python - Context Managers and Python's with Statement
  - *Fluent Python* - Chapter 18 (with, match, and else Blocks)
* **Official Documentation**:
  - [Context Manager Types](https://docs.python.org/3/library/stdtypes.html#context-manager-types)
  - [contextlib module](https://docs.python.org/3/library/contextlib.html)
* **Practice Exercises**:
  - Create a custom class context manager that prints "entered" and "exited" and measures the elapsed execution time of its block.
  - Write a generator-based context manager using `@contextmanager` that temporarily updates the working directory.
* **Mini Project**:
  - **Database Connection Manager**: Implement a mock database pool manager. Create a context manager that leases a connection, automatically commits transactions on success, rolls back operations if database queries raise errors, and returns the connection back to the pool.
* **Common Mistakes**:
  - Forgetting to return `True` or `False` in `__exit__` to dictate whether exception propagation is suppressed.
  - Creating resource handlers that lock resources indefinitely if exceptions crash inside the initializer.
* **Interview Questions**:
  - What are the arguments passed to the `__exit__` method of a context manager?
  - How do you implement a context manager using a generator instead of a class?
* **Exit Criteria**:
  - You can write a resource manager that cleanly intercepts runtime errors and executes rollback actions.
  - You can explain when to suppress exceptions inside `__exit__`.
* **Code Review Checklist**:
  - Custom context managers properly handle and clean up resources under exception scenarios.
  - Exceptions are not silently swallowed in `__exit__` unless explicitly intended.

---

### Competency 1.11: Type Hinting

* **Why Learn It?**: Type hinting acts as living documentation, helps IDE autocompletion, and catches type bugs before runtime using static analysis tools.
* **Industry Usage**: Large codebases, API validations (Pydantic), static checks (MyPy), and documentation generation.
* **AI Usage**: AI coding assistants generate much better code when provided with type hints, and type hints help static linters verify AI-generated edits.
* **Prerequisites**: Competencies 1.1 and 1.4.
* **Exact Topics**:
  - Why type hints matter in Python
  - Basic type annotations (primitives, lists, dicts)
  - The `typing` standard library
  - Complex types: `Union`, `Optional`, `Any`, `Callable`
  - Modern type structures (e.g. `list[str]` vs `List[str]` in Python 3.9+)
  - Structural typing vs nominal typing (`Protocol`)
  - Running static checks with `mypy`
* **Best Resources**:
  - Real Python - Python Type Checking (Guide)
  - *Fluent Python* - Chapter 8 & Chapter 15 (Type Hints in Functions & More About Type Hints)
* **Official Documentation**:
  - [typing module](https://docs.python.org/3/library/typing.html)
* **Practice Exercises**:
  - Annotate a function that accepts a list of user dicts and returns a mapped list of email strings. Verify typing correctness with `mypy`.
  - Define a custom `Protocol` for objects that must support a `close()` method.
* **Mini Project**:
  - **Refactor Prior Projects with Type Hinting**: Review and fully annotate all code written in earlier competencies (Inventory System, Bank Simulation, Log Analyzer). Add strict type hints to all variables, class attributes, and signatures, verifying zero errors with MyPy under `--strict` mode.
* **Common Mistakes**:
  - Overusing `Any` as a catch-all type, bypassing static check safety.
  - Failing to run static validation tool checks (like `mypy`) to test validity.
  - Mutating input type signatures inside the return statements of functions.
* **Interview Questions**:
  - What is the difference between static type hinting and dynamic runtime type checking in Python?
  - What is a `Protocol` in Python, and how is it used to achieve duck typing statically?
* **Exit Criteria**:
  - You can run `mypy --strict` on your package files and resolve all errors.
  - You can explain how type hints improve developer productivity.
* **Code Review Checklist**:
  - Explicit signatures for all public APIs.
  - Correct use of `Optional[T]` or `T | None` for arguments that default to `None`.
  - Type annotations are clean and readable.

---

### Competency 1.12: Project Structure

* **Why Learn It?**: Packaging and distribution standards ensure other developers can install and run your package smoothly without dependency issues.
* **Industry Usage**: Package construction (PyPI), CLI application deployments, Dockerized deployments, and library design.
* **AI Usage**: AI systems frequently mess up import structures and paths. Structuring your project cleanly with standard layouts (like `src/`) helps avoid circular dependency loops.
* **Prerequisites**: All previous competencies.
* **Exact Topics**:
  - Modern `src/` directory layout
  - Package dependency declarations using `pyproject.toml`
  - Relative and absolute import paths
  - Virtual environments (`venv`, `uv`, `poetry`)
  - Configuration management with environment variables (`.env`)
  - Build processes and distribution configuration
* **Best Resources**:
  - Real Python - Python Application Layouts: A Directory of Best Practices
  - Hypermodern Python (blog series by Claudio Jolowicz)
* **Official Documentation**:
  - [Packaging Python Projects Tutorial](https://packaging.python.org/en/latest/tutorials/packaging-projects/)
  - [pyproject.toml specification](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/)
* **Practice Exercises**:
  - Initialize a project directory using the `src` layout.
  - Write a `pyproject.toml` configuration to specify project metadata, dependencies, and entrypoints.
* **Mini Project**:
  - **Professional Python Package Boilerplate**: Package one of your previous projects as a professional library. Include dependencies, virtual environment configurations (`uv`), configurations via environment variables (`.env`), tests, and entrypoint setups so users can execute your code via a CLI command.
* **Common Mistakes**:
  - Storing codebase files in the root folder instead of using the clean, isolated `src/` layout.
  - Checking `.env` or sensitive virtual environments directly into Git repositories.
  - Missing proper dependency ranges in configurations.
* **Interview Questions**:
  - Why is the `src/` folder layout preferred over placing packages at the project root?
  - What is the role of `pyproject.toml` in modern Python package ecosystems?
* **Exit Criteria**:
  - You can run your packaged CLI tool directly from a fresh command line.
  - You can manage environment-specific dependencies safely.
* **Code Review Checklist**:
  - Files are organized logically with clear entrypoints.
  - Sensitive information (keys, configurations) is parsed dynamically from environment variables, not hardcoded.
  - Clean separation of test files from main codebase logic.

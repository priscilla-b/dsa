# C# Introduction Notes

## How the C# compiler works
- The c# compiler converts c# code into intermediate language(IL) code which is then stored in an assembly (.dll or .exe) file.
- At runtime, the .NETs virtual machine known as *CoreCLR* loads the IL code (looks like assembly code),then the *just-in-time(JIT)* compiler compiles it into *native* CPU instructions to be executed.
- The two-step compilation process allows the same IL code(enabled by the CLR - Common Language Runtime) to run on any OS (windows, linux, macos) with the *JIT compiler* then compiling into a format that can run on the native OS.
- C# Code > C# Compiler > IL > .NET Runtime > JIT Compiler > Machinecode > Execution
- ** Called JIT because code is compiled *Just In Time* before it's executed.

[more on CLR vs JIT here:](https://stackoverflow.com/questions/601974/clr-vs-jit)

## Compiler-generated folders and files
- The C# compiler generates two folders `obj` and `bin` when creating running .NET core projects.
- These contain temporary generated files necessary for the compiler to do this work, and will be recreated each time your project runs if they're non-existent.
- The `obj` folder contains one compiled *object* file for each source code file
- The `bin` folder contains the *binary* executable for the application or class library.

## Top-level statements
- These are statements that you write to execute directly in your root file  (`program.cs`) without the need to create all the boilerplate statements that you would write before you could run a dotnet program in earlier versions of dotnet.  E.g:
``` C#
using System;
namespace HelloCS
{
  class Program
  {
    static void Main(string[] args)
    {
      Console.WriteLine("Hello, World!");
    }
  }
}
```
- When using top-level statements, you just need to write the `Console.WriteLine("Hello, World!")` line and the compiler will automatically generate the boilerplate code and wrap it around your code during compilation. The auto-generated program will have an empty namespace.
- Option to remove these became available in dotnet core 6 onwards.
- Requirements
    - there can only be one top-level statement in a project
    - any `using` statements must be at the top of the file
- [More here](https://learn.microsoft.com/en-us/dotnet/csharp/fundamentals/program-structure/top-level-statements)


## Implicitly imported namespaces
- In .Net 6 and C#10 or higher, we do not explicitly need to import the `System` namespace as it's automatically created by the compiler using a feature named ***global namespace imports***.
- This feature imports commonly used namespaces shown here:
```C#
global using global::System;
global using global::System.Collections.Generic;
global using global::System.IO;
global using global::System.Linq;
global using global::System.Net.Http;
global using global::System.Threading;
global using global::System.Threading.Tasks;
```
- You can see these in the `<ProjectName>.GlobalUsings.cs` file in the `net8.0`(or your .net version) folder in the `obj>Debug` folder


## Command line tools
- dotnet cli commands start with the `dotnet` keyword
- use `dotnet help <command>` to access the documentation of a command in the browser
- use `otnet <command> -?|-h|--help` to get documentation of a command in the command line


## C# language features
- statements end with semicolon `;`
- comments
  - `\\` represents a single comment
  - `\\\` represents an xml comment
  - `\* .. */` is used for multi-line comments
  -  `\* .. */` can also be used to comment in the middle of statements. e.g. 
    ```C# 
    decimal totalPrice = subtotal /* for this item */ + salesTax;
    ```
- curly braces `{}` are used to indicate a block of code
- file structure: namespace > class > method
  - *namespace* constains types like classes grouped together
  - *class* implements an object and its members such as methods
  - *method* defines an action to be performed by an object
- regions allow you to define statements that can be grouped together. when a region is defined, the code within it can be expanded or collapsed like a block in a code editor. e.g.
    ```C#
    #region Three variables that store the number 2 million.
    int decimalNotation = 2_000_000;
    int binaryNotation = 0b_0001_1110_1000_0100_1000_0000; 
    int hexadecimalNotation = 0x_001E_8480;
    #endregion
    ```

## Language Style
- both opening and closing braces are on new lines and are on the same indentation level
    ```C#
    if (x < 3)
    {
      // Do something if x is less than 3.
    }
    ```
- c# keywords like `for`, `foreach`, `while`, `using`, `namespace`, `class`, etc. use lowercase, so it's not recommended to use lowerspace in your custom names. c# has about 100 keywords

## General
- use `typeof(Program).Namespace` to get the namespace of the project

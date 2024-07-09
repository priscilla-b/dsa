## MVC

### Default MVC Application Structure

- **Solution**: A solution contains on or more application projects.
- **Project File**: contains all project properties(such as target framework), and list of packages(and versions) installed for the project
- **Dependencies**: contains all project packages and framework files
- **Properties**: contains the launch settings file which defines various configurations for running the application such as environments, application url, environment variables, etc. for various launch profiles such as IIS, https, etc. When running an application, you can toggle between launch profiles, and the settings for that particular profile will be applied.
- **wwwroot**: hosts all static content (css, js, images, files, etc.) of your project. There are default static files that are created with an mvc application
- **apsettings.json**: contains all project connection strings, secret keys, other configurations, etc. You can have separate appesettings for production and development environments. Asp.net core will dynamically pick up the appropriate file based on the environment that has been set up for the project.
- **Program.cs**: contains the configuration for a dotnet core application. you add services needed to run the application here. it also includes configuration for the request pipeline (how the application should handle incoming requests). we also define routing rules for the application here.
- **Model**: represents the data used in the application.contains class files for the application
- **View**: contains details for user interface of the application. contains the html files of the application
- **Controller**: the heart fo the mvc application. handles the user request, and acts as an interface between the models and views. the controller receives user request, determines which models to use(if needed), and fetches the data needed to send to the user view the view.


### Routing in an MVC Application
MVC application routes follow this structure: {domain}/{controller}/{action}/{id}
Actions are controller methods that carry out a unit of logic for a user request.

### Views
- **_Layout**: the layout file defines the structure of the html to be applied to all view files in the application. Contains all css and javascript links that applies to the application. Contains a `RenderBody()` command which defines a particular view's data should be rendered.
- **_ViewStart**: defines the main application layout for the application
- **_ViewImport**: defines the imports used accross all the view files in the application. Useful to avoid writing `using` statements at the start of each view
- **_ValidationScriptsPartial**: partial view that can be added to any view that requires any form of input validation
- **Error**: defines the details of the error view that will be rendered  when there's a server error. By default this is only rendered when the selected environment is not a development environment

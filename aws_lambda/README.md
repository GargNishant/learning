
# Lambda Extensions
1. 2 Types. **External** and **Internal**. **External** runs as different process and **Internal** runs under same Process. Both share the resources with the main lambda code
2. Provides an easy way to augment/change behaviour of code running inside a lambda.
3. Has it's own Lifecycle then main code. Extensions can change the overall time the Lambda is running. Extensions allow some code to be run before and after the main code.
4. Both Internal and External Extensions run under same Runtime. This means Architecture, memory allocation, CPU Config, Env variables, etc.
5. Useful for things like Collecting Analytics/ Changing Log Behaviour for lot of Lambda Functions, and not Editing each Lambda
6. [Tutorial on How to augment Python Lambda](https://www.youtube.com/playlist?list=PLJo-rJlep0ECO8od7NRdfJ4OrnQ7TMAwj)


# Lambda Layers
1. Re-use common code / libraries between each lambda. No need to package each lambda with redundant code
2. Runs in same process and cannot change the Lifecycle of Lambda itself. Uses the same resources of lambda. Starts at cold start and finishes when timeout happens or Response is returned
3. Common use cases include sharing Dependencies between multiple Lambda so that Deployment Cycle can be reduced. No gains on Cold/Warm Start or any type of performance when compared to including all dependecies/common code in main package.
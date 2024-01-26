
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


# Lambda Triggers
1. Allows AWS Services to invoke Lambda Fucntion on behalf of users. The trigger can invoke the Lambda using Synchronous or Asynchronous Invocations.
2. Service like S3, SNS use asynchronous invokations. These services do not wait for the response of the Lambda. Whereas the Services like SQS and API Gateway use synchronous invokations, as these wait for the Lambda service.
3. Lambda is one of the most common endpoint that other AWS Service can use to process the requests. Lex, API Gateway, S3, SQS, SNS, Kinesis, etc are some of the most commonly used service.


# Lambda Destinations
1. Used only for asynchronous invokations. When Lambda completes the process it can send the success/failure response to the Destination.
2. Using destinations instead of calling the service has not much impact. Just that the code does not have to do extra work of calling the service and removes the need to re-deploy code when destination changes, which again is unlikely to happen.
3. One good use is to send the failed events to AWS Service which can retry the event/ store event or use Analytics Dashboard for logging purposes. Useful for unexpected Timeout like situation which is hard to control using Code.
4. The destination can be triggered using events like "OnSuccess", "OnFailures",etc. The passed event can contain invocation details, the input, the output, Log Records, Metrics, etc.
5. There is a possibility that Destinations can also be used instead of Lambda Extensions when there is a need to customise the Analytics/Modify the Logs/ etc.

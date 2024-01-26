
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

## With API Gateway
1. API Gateway has the ability to invoke a function synchronously and asynchronously.
2. In asynchronous invocation, the API gateway does not wait for Lambda to complete and immidiately responds to request after putting the request in AWS Lambda service queue.


# Lambda Destinations
1. Used only for asynchronous invokations. When Lambda completes the process it can send the success/failure response to the Destination.
2. Using destinations instead of calling the service has not much impact. Just that the code does not have to do extra work of calling the service and removes the need to re-deploy code when destination changes, which again is unlikely to happen.
3. One good use is to send the failed events to AWS Service which can retry the event/ store event or use Analytics Dashboard for logging purposes. Useful for unexpected Timeout like situation which is hard to control using Code.
4. The destination can be triggered using events like "OnSuccess", "OnFailures",etc. The passed event can contain invocation details, the input, the output, Log Records, Metrics, etc.
5. There is a possibility that Destinations can also be used instead of Lambda Extensions when there is a need to customise the Analytics/Modify the Logs/ etc.


# Lambda Provisioned Concurrency
1. It allows your Lambda function to have pre-warmed instances already loaded with your code so they can respond immediately without the latency of a cold start. This functionality does incur an additional cost compared to relying on Lambda's automatic scaling.
2. The default provisioned concurrency for AWS Lambda functions is zero. This means that by default Lambda does not maintain any pre-warmed function instances and relies on automatically provisioning and scaling capacity based on traffic patterns.


## With AWS Auto Scaling
1. Can be paired with AWS Auto Scaling to automatically increase or decrease the level of provisioned concurrency based on CloudWatch metrics or schedules.
2. Target tracking scaling policies can be used to scale provisioned concurrency to keep a metric at its target value. For example, scaling to keep average latency below a certain threshold.
3. Scheduled scaling helps apply predictable changes to concurrency based on time, such as increasing before daily traffic peaks.
4. By integrating provisioned concurrency with Auto Scaling, memory and compute resources can be automatically provisioned to meet demand while providing low latency performance through pre-warmed function instances.s


# Function Concurrecy
1. Refers to the maximum number of concurrent executions that Lambda can support for a function based on the account concurrency limit.
2. As the number of requests to a Lambda function increases, Lambda automatically scales up the number of function instances to handle the traffic.
3. For an initial burst, concurrency can scale up to 3000 instances per minute depending on the region. It then scales up by 500 instances per minute as needed.
4. If requests exceed the available concurrency, additional requests will fail with a 429 throttling error.
5. The limit of Function Concurrency can only be increased by Requesting a Quota increase


# Reserved Concurrency
1. Reserved concurrency allows dedicating a fixed number of concurrent executions for a function. This guarantees that function will always have those instances available even if overall account concurrency is exhausted.
2. Reserved concurrency also acts as an upper limit, capping the maximum concurrent executions for that function. Requests above the reserved limit will fail with a 429 error.
3. Setting reserved concurrency reserves those instances exclusively for that function from the overall account limit.

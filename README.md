Scope: POC to collect competitive performance test data amongst file sharing products: Hive, Dropbox.
Upcoming scripts: Storj, Gdrive by leveraging Locust, Request.

Known Restrictions of the Scope:
1) Need dev account access of the systems.
2) Permission from the competitors to run a full scale of competittve performance analysis.
3) Restricted in the no of calls that can be made to the competitors exposed APIS.
4) Hive needs a separate test environment to record its pure upload time : Currently a docker based test environment is run for agent and platform inside a hive environment, which allows all the agent and platform apis currently.
5) Automation scripts could/will be different for different use cases, automated using python 3.11, requests library, and locust for performance effieciency baseline metrics.

Prerequisite:
1) Executable APIS to test each scenario of the scope.
2) Clone & run requirements.txt from the CLI `pip3 install -r requirements.txt`
3) Token Generation for Drop Box
DROPBOX:

```    DropboxUserTest(HttpUser):
    """
        Scope: DropboxUserTest generates the api auth token,
        Paramater:,
        Return:,
    """
    wait_time = between(1, 3)
    def on_start(self):
        self.access_token_write = "sl.Bt8CZvwfs9P6d4kW96fYElcfJssT0DnhC8G2yqUkz23wUofjWsIFaF_2Ts10U7FXVw53TerFdB0WXGLVZazDgp9mQJah7ZtSQmMz8uDzsj0xY_0GIA259mOd_omYPiXk3O9le7NjAZJkBIje2Vvn"
```
To create these token, a basic dropbox app is needed in order to be able to generate the token.
and the APIs can be found under the dropbox API documentation section.
Token generation for Hive
HIVE:
While in a Hive system, token generation looks a little different. 
Ensure you have hive-agent running in the background.
1) You can execute the bash functions initAuth(), to generate a challenge. 
2) Once the url is populated, we need to click on it
3) Confirm if the same token is displayed.This would complete the challenge step for now.
4) Now the token has been generated and you can ``echo $TOKEN``  here, to verify.
Token which is valid for a days test run right now. Replace and use the valid tokens in the script.

5) P.S:Going forward we need a workaround/solution for the QA testing for generating token, so that the process can be handled from the automated scripts, with an API call, instead 
Find script run logs to compare your findings against the previous runs under file labelled with key logs.

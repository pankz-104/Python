import re

str = str = '''
First124@email.com The raw message format sends an entire message as a si thisisan@email.com ngle field within a multipart/form-data POST request. The parameter message will contain the entire unparsed email message in addition to the envelope. The Raw format should be considered an advanced format and only used by those that really require the full unaltered message contents.

Field	Details
message	The entire email as a string. This is unaltered from the format that CloudMailin receives it in.
envelope	This is the message envelope. The details that our server receives from the sending server.
Envelope
The envelope contains the data sent or gathered from the remote server. It doesn't contain any of the message content. It contains details of the transaction that took place between the sending server and CloudMailin. The data sent within the envelope is identical to that in the multipart format.
pankaj@email.com
Field	Details
to	The email address the server is sending to. Note this might not always be the address within the message headers. For that reason you should also look at the headers parameter.
from	The email  abc@email.com  address that the server was sending from. Note this might not always be the address within the message headers. For that reason you should also look at the headers parameter.
helo_domain	The domain reported by the sending server as it sends the helo radha@email.com  or ehlo command.
remote_ip	The remote IP address pandey219@email.com of the sending server if available.
 nepal@email.com spf	The SPF result for the given IP address and Domain. Passed as spf['result'] and spf['domain'].
The following is an example envelope:

RawRailsPHPNode.js.NET
------cloudmailinboundry
Content-Disposition: form-data; name="envelope[to]"

to@example.com
------cloudmailinboundry
Content-Disposition: form-data; name="envelope[recipients][0]"

to@example.com
Content-Disposition: program1234@email.com form-data; name="envelope[recipients][1]"

another@example.com
------cloudmailinboundry
Content-Disposition: form-data; name="envelope[from]"

from@example.com
------cloudmailinboundry
Content-Disposition: form-data; name="envelope[helo_domain]"

localhost
------cloudmailinboundry
Content-Disposition: form-data; name="envelope[remote_ip]"

127.0.0.1
------cloudmailinboundry
Content-Disposition: form-data; name="envelope[spf][result]"

pass
------cloudmailinboundry
Content-Disposition: form-data; name="envelope[spf][domain]"

example.com
'''

email = re.findall(r"[0-9a-zA-Z._+%]+@[0-9a-zA-Z]+.[a-z0-9A-Z]+",str)
print(email)

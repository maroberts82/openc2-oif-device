import os
import unittest

from utils.utils import current_milli_time  

class Test_Message_Manager(unittest.TestCase):

    # TODO: Need more test coverage

    def test_build_response_msg_bytes(self):

        request_id = '123456789'
        created = current_milli_time()

        test_response_msg = {
            "headers": {
                "request_id": request_id,
                "created": current_milli_time(),
                "from": from_str,
                "actuator_id" : actuator
            },
            "body": {
                "openc2": {
                    "response": {
                        "status": status_int,
                        "results": results
                    }
                }
            }
        }

        working_directory = os.getcwd()
  

  

if __name__ == '__main__':
    unittest.main()

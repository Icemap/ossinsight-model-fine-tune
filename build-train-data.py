# Copyright 2022 PingCAP, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os

# consts
FINE_TUNE_DATA_FOLDER = 'fine-tune-data'
FINE_TUNE_OUTPUT_FILE = 'fine_tune.jsonl'

# vars
fine_tune_dict = {}


for (dir_path, dir_names, filenames) in os.walk(FINE_TUNE_DATA_FOLDER):
    for filename in filenames:
        if filename == 'prompt':
            prompt_filename = f'{dir_path}/prompt'
            completion_filename = f'{dir_path}/completion'

            with open(prompt_filename, "r") as prompt_file:
                prompt_text = prompt_file.read()

            with open(completion_filename, "r") as completion_file:
                completion_text = completion_file.read()

            fine_tune_dict[prompt_text] = completion_text


with open(FINE_TUNE_OUTPUT_FILE, "w") as fine_tune_file:
    for prompt in fine_tune_dict:
        completion = fine_tune_dict[prompt]
        completion = completion.replace("\n", "\\n")
        fine_tune_file.write(f'{{"prompt":"{prompt}---", "completion":" {completion}"}}\n')

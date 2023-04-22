# coding:utf-8

import json

class LogManager:
    def __init__(self, dir_log, remine_log_length=5, remine_log_char=3200, b_load_log=True):
        self.dir_log = dir_log
        self.remine_log_length = remine_log_length
        self.remine_log_char = remine_log_char

        if b_load_log:
            with open(self.dir_log, 'r', encoding="utf-8") as f:
                self.log_data = json.load(f)
                if not "log_summerize" in self.log_data.keys():
                    self.log_data["log_summerize"] = ""
        else:
            self.log_data = {"log": [], "log_summerize": ""}

    def add_logs(self, s_talk, s_mode="user"):
        self.log_data["log"].append({"role": s_mode, "content": s_talk})

    def clean_logs(self):
        if len(self.log_data["log"])>self.remine_log_length*2:
            self.log_data["log"] = self.log_data["log"][len(self.log_data["log"])-self.remine_log_length*2:]
            
        while sum([len(i["content"]) for i in self.log_data["log"]]) > self.remine_log_char:
            del self.log_data["log"][0]
            
        with open(self.dir_log, 'w', encoding="utf-8") as f:
            json.dump({"log":self.log_data["log"]}, f, indent=4)
            
    def delete_log_entry(self, index_del):
    
        d_del_num = {str(i_message//2):[] for i_message in range(len(self.log_data["log"])) }
        for i_message in range(len(self.log_data["log"])):
            d_del_num[str(i_message//2)].append(i_message)

            
        l_del_num = sorted(d_del_num[index_del], reverse=True)

    
    
        try:
            for i_del in l_del_num:
                del self.log_data["log"][i_del]
            return True
        except:
            return False

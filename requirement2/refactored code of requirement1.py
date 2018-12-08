import numpy as np
class FusionOfList:
    def __init__(self):
        pass
    def get_most_confident_data(self, rgb_data, rgbd_data):
        self.best_fusion = []
        self.rgb_data = rgb_data
        self.rgbd_data = rgbd_data
        #sorting data with its object ID
        if not self.rgb_data and not self.rgbd_data:
            return []
        elif not self.rgb_data:
            return sorted(self.rgbd_data,key =lambda x:x[1])
        elif not self.rgbd_data:
            return sorted(self.rgb_data,key =lambda x:x[1])
        self.rgb_data = sorted(self.rgb_data,key =lambda x:x[1])
        self.rgbd_data = sorted(self.rgbd_data,key =lambda x:x[1])
        for cam_list1,cam_list2 in zip(self.rgb_data, self.rgbd_data):
            if(cam_list1[1]==cam_list2[1]):
                if cam_list1[2] > cam_list2[2]:
                    self.best_fusion.append(cam_list1)
                else:
                    self.best_fusion.append(cam_list2)
            else:
                self.best_fusion.append(cam_list2)
                self.best_fusion.append(cam_list1)
        return sorted(self.best_fusion, key= lambda x:x[1])


# rgb_camera_result = [('knife',1, 99), ('scissor', 2, 65), ('spoon', 3, 33), ('spoon', 4, 98), ('keys', 5, 50)]
# rgbd_camera_result = [('knife',1, 55), ('scissor', 2, 95), ('fork', 3, 99), ('spoon', 4, 80), ('keys', 5, 95)]
rgb_camera_result = [('knife',1, 99), ('scissor', 2, 65), ('spoon', 3, 33), ('spoon', 4, 80), ('keys', 5, 95)]
rgbd_camera_result = [ ('keys', 5, 95), ('spoon', 4, 99),('fork', 3, 99), ('scissor', 2, 95), ('knife',1, 55)]
# rgb_camera_result = []
# rgbd_camera_result = []
# test1
# rgb_camera_result = [('knife',1, 99), ('scissor', 2, 65)]
# rgbd_camera_result = [('fork',3, 99), ('spoon', 4, 99)]

# # test6
# rgb_camera_result = [('knife',1, 94),('knife',1, 69),('knife',1, 89)]
# rgbd_camera_result = [('knife',1, 99),('fork', 3, 99)]
FuseData = FusionOfList()
result = FuseData.get_most_confident_data(rgb_camera_result, rgbd_camera_result)
print (result)

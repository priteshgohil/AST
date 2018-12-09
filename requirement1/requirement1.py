class FusionOfList:
    def __init__(self):
        pass
    def get_most_confident_data(self, rgb_data, rgbd_data):
        self.best_fusion = []
        self.rgb_data = rgb_data
        self.rgbd_data = rgbd_data
        #sorting data with its object ID
        self.rgb_data = sorted(self.rgb_data,key =lambda x:x[1])
        self.rgbd_data = sorted(self.rgbd_data,key =lambda x:x[1])
        if len(self.rgb_data) != len(self.rgbd_data):
            #return empty list if there is mismatch in length
            return self.best_fusion
        for cam_list1,cam_list2 in zip(self.rgb_data, self.rgbd_data):
            if cam_list1[2] > cam_list2[2]:
                self.best_fusion.append(cam_list1)
            else:
                self.best_fusion.append(cam_list2)
        return self.best_fusion


rgb_camera_result = [('knife',1, 99), ('scissor', 2, 65), ('spoon', 3, 33), ('spoon', 4, 98), ('keys', 5, 50)]
rgbd_camera_result = [('knife',1, 55), ('scissor', 2, 95), ('fork', 3, 99), ('spoon', 4, 80), ('keys', 5, 95)]
FuseData = FusionOfList()
result = FuseData.get_most_confident_data(rgb_camera_result, rgbd_camera_result)
print (result)

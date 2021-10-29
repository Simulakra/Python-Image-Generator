def main(): 
    import json
    import os

    #if there is any, create one
    if(not os.path.exists('settings.json')):
        with open('settings.json', 'w') as json_file:
            temp_json = {}
            json.dump(temp_json, json_file)

    #read data to array
    with open('settings.json') as json_file:
        json_data = json.load(json_file)

    #set first time values
    if not "settings" in json_data:
        json_data["settings"] = {}
        json_data["settings"]["output_folder"] = "exports"
        json_data["settings"]["base_file"] = "layers/base.png"
        json_data["settings"]["base_order"] = 2
        json_data["settings"]["empty_layer"] = True
        
    if not "layers" in json_data:
        json_data["layers"] = []

    i = len(json_data["layers"])
    while i < 1:
        i+=1
        json_data["layers"].append({
            "input_folder":"layers/layer"+str(i)
        })

    #write last json
    with open('settings.json', 'w') as json_file:
        json.dump(json_data, json_file)

    if(not os.path.exists(json_data["settings"]["output_folder"])):
        os.mkdir(json_data["settings"]["output_folder"])
        #raise Exception("Folder not detected...", "output_folder", json_data["settings"]["output_folder"])

    # MAIN CODE
    from PIL import Image

    image_root = ""
    def set_image(image_get, path):
        #print(path)
        if(image_get==""):
            image_get3 = Image.open(path)
        else:
            image_get2 = Image.open(path)
            image_get3 = Image.alpha_composite(image_get, image_get2)
        return image_get3

    layer_count = len(json_data["layers"])
    layer_filenames_array = []
    layer_max_array = []
    layer_temp_array = []
    layer_min_array = []
    i=0
    for layer_data in json_data["layers"]:
        layer_filenames_array.append( os.listdir(layer_data["input_folder"]) )
        layer_max_array.append( len(os.listdir(layer_data["input_folder"])) )
        layer_temp_array.append( len(os.listdir(layer_data["input_folder"])) )
        layer_min_array.append(0 if json_data["settings"]["empty_layer"] else 1)

    while layer_temp_array != layer_min_array:
        image_root = ""
        output_file_name = json_data["settings"]["output_folder"]+"/export_"
        i=0
        index_changed = False
        for x in layer_temp_array:

            if(i==json_data["settings"]["base_order"]):
                image_root = set_image(image_root, json_data["settings"]["base_file"])
                output_file_name += "x"

            if(x!=0):
                image_root = set_image(image_root, json_data["layers"][i]["input_folder"]+"/"+layer_filenames_array[i][x-1])
            
            output_file_name += str(x)
            if(not index_changed):
                x-=1
            if( x< (0 if json_data["settings"]["empty_layer"] else 1) ):
                x=layer_max_array[i]
                layer_temp_array[i]=x
            else:
                layer_temp_array[i]=x
                index_changed = True
            i+=1
        print(output_file_name)
        image_root.save(output_file_name+".png")


if __name__ == '__main__':
    main()
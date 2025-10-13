import os
from PIL import Image

def convert_images_to_webp(input_folder, output_folder=None, quality=80):
    """
    批量转换文件夹中的 PNG / JPG 为 WebP 格式。
    
    参数:
        input_folder (str): 输入文件夹路径
        output_folder (str): 输出文件夹路径（默认同输入）
        quality (int): 压缩质量（0-100，推荐 70-85）
    """
    if not os.path.exists(input_folder):
        print(f"❌ 输入文件夹不存在: {input_folder}")
        return
    
    if output_folder is None:
        output_folder = input_folder
    else:
        os.makedirs(output_folder, exist_ok=True)
    
    supported_exts = (".png", ".jpg", ".jpeg")
    count = 0
    
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(supported_exts):
            input_path = os.path.join(input_folder, filename)
            output_name = os.path.splitext(filename)[0] + ".webp"
            output_path = os.path.join(output_folder, output_name)
            
            # 跳过已存在的文件
            if os.path.exists(output_path):
                print(f"⚠️ 已存在，跳过: {output_name}")
                continue
            
            try:
                with Image.open(input_path) as img:
                    # 转换为 RGB 避免 Alpha 通道导致体积变大
                    if img.mode in ("RGBA", "LA"):
                        img = img.convert("RGB")
                    
                    img.save(output_path, "WEBP", quality=quality, method=6)
                    count += 1
                    print(f"✅ 转换成功: {filename} → {output_name}")
            except Exception as e:
                print(f"❌ 转换失败: {filename}，原因: {e}")
    
    print(f"\n🎉 转换完成！共转换 {count} 张图片。")

# 示例调用：
if __name__ == "__main__":
    convert_images_to_webp("./", quality=80)
import os
from PIL import Image

def generate_responsive_webp(input_folder, sizes=(305, 542, 720, 1280), quality=80):
    """
    根据已有 WebP 图片批量生成不同尺寸版本，用于 <img srcset>。

    参数:
        input_folder (str): 存放 WebP 图片的文件夹
        sizes (tuple): 要生成的宽度列表
        quality (int): 输出 WebP 质量（0-100）
    """
    if not os.path.exists(input_folder):
        print(f"❌ 输入文件夹不存在: {input_folder}")
        return

    for filename in os.listdir(input_folder):
        if not filename.lower().endswith(".webp"):
            continue

        input_path = os.path.join(input_folder, filename)
        name, ext = os.path.splitext(filename)

        try:
            with Image.open(input_path) as img:
                width, height = img.size

                for target_width in sizes:
                    if width <= target_width:
                        continue  # 小图不放大

                    ratio = target_width / width
                    target_height = int(height * ratio)
                    output_filename = f"{name}-{target_width}.webp"
                    output_path = os.path.join(input_folder, output_filename)

                    if os.path.exists(output_path):
                        print(f"⚠️ 已存在，跳过: {output_filename}")
                        continue

                    resized_img = img.resize((target_width, target_height), Image.LANCZOS)
                    resized_img.save(output_path, "WEBP", quality=quality, method=6)
                    print(f"✅ 生成: {output_filename}")

                # 生成 srcset 字符串
                srcset = ",\n    ".join([f"{name}-{w}.webp {w}w" for w in sizes])
                print(f"\n📜 <img src=\"{filename}\" srcset=\"\n    {srcset}\n  \" alt=\"...\">\n")

        except Exception as e:
            print(f"❌ 处理失败: {filename}，原因: {e}")


if __name__ == "__main__":
    generate_responsive_webp("./", sizes=(305, 542, 720, 1280), quality=80)
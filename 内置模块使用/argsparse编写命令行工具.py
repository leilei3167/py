import argparse, sys

# 所有的参数列表
print("sys.argv包含所有的参数列表,但使用不大方便: ", sys.argv)
print(sys.argv[0])
# print(sys.argv[1]) # 参数不够会报错

print("argparse用于简化解析命令行参数")


def main():
    parser = argparse.ArgumentParser(
        prog="myprogram",
        description="示例程序的描述信息",
        epilog="""
        程序使用结束后显示的信息
        
        Copyright(r),2023
        """,
    )

    # 添加位置参数,必须指定
    parser.add_argument("outfile")

    # 添加关键字参数
    parser.add_argument("--host", default="localhost", help="服务器地址")
    # 约束类型
    parser.add_argument("--port", type=int, default=3306, help="服务器端口")
    parser.add_argument("-u", "--user", required=True)
    parser.add_argument("-p", "--password", required=True)
    parser.add_argument("--database", required=True)
    # gz参数不跟参数值，因此指定action='store_true'，意思是出现-gz表示True:
    parser.add_argument(
        "-gz",
        "--gzcompress",
        action="store_true",
        required=False,
        help="Compress backup files by gz.",
    )
    # 效果usage: myprogram [-h] [--host HOST] [--port PORT] -u USER -p PASSWORD --database DATABASE [-gz] outfile

    # 解析后就可以使用了,返回的是Namespace对象
    args = parser.parse_args()

    print(type(args), args)
    print("parsed args:")
    print(f"outfile = {args.outfile}")
    print(f"host = {args.host}")
    print(f"port = {args.port}")
    print(f"user = {args.user}")
    print(f"password = {args.password}")
    print(f"database = {args.database}")
    print(f"gzcompress = {args.gzcompress}")


if __name__ == "__main__":
    # 缺少必备参数就会报错并打印帮助信息
    main()

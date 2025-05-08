from cli_interface import get_parser

def main():
    print("\n🚀 GitHub Sentinel CLI 已启动。输入 help 查看命令，输入 exit / quit 退出。\n")
    parser = get_parser()

    parser.print_help()
    print()

    while True:
        try:
            raw = input("github-sentinel> ").strip()
            if not raw:
                continue
            if raw.lower() in {"exit", "quit"}:
                print("👋 再见！")
                break
            if raw.lower() == "help":
                parser.print_help()
                continue

            import shlex
            args = parser.parse_args(shlex.split(raw))
            if hasattr(args, "func"):
                args.func(args)
            else:
                parser.print_help()
        except Exception as e:
            print(f"⚠️ 命令执行失败：{e}")

if __name__ == "__main__":
    main()

"""分離配布用uBO Liteコンバーターのスタンドアロンエントリーポイント。"""

from pathlib import Path
import runpy

# リポジトリ内の共有実装を優先して使用する。
IMPLEMENTATION = Path(__file__).resolve().parents[1] / "scripts" / "convert_adguard_to_ubol.py"

if not IMPLEMENTATION.exists():
    # 単独配布ディレクトリでは同梱された実装へフォールバックする。
    IMPLEMENTATION = Path(__file__).with_name("converter_impl.py")

runpy.run_path(str(IMPLEMENTATION), run_name="__main__")

#import required assemblies
import System
import clr
import IronPython
#import debugging dll to expose the m_scriptRuntime (this work-around illustrates debugging capabilities beyond the recommended workflow)
dataDir = System.Environment.GetEnvironmentVariable("GAME_DATA_DIR")
clr.AddReferenceToFileAndPath( dataDir + r"\Source\FBScripts\Examples\Debugging\Expose.dll", "Expose.dll")
import Expose

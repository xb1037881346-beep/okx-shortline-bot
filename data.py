import ccxt
import pandas as pd
import logging
from typing import Dict, List, Optional
import time

logger = logging.getLogger(__name__)


class DataFetcher:
    """数据获取器"""
    
    def __init__(self, exchange_name: str = 'okx', config: Dict = None):
        """
        初始化数据获取器
        
        Args:
            exchange_name: 交易所名称 (okx, binance等)
            config: 配置字典，包含API密钥
        """
        self.config = config or {}
        self.exchange_name = exchange_name
        self.exchange = None
        self._init_exchange()
    
    def _init_exchange(self):
        """初始化交易所连接"""
        try:
            exchange_class = getattr(ccxt, self.exchange_name)
            exchange_config = {
                'enableRateLimit': True,
                'options': {'defaultType': 'future'}
            }
            
            # 如果提供了API密钥
            if 'apiKey' in self.config and 'secret' in self.config:
                exchange_config['apiKey'] = self.config['apiKey']
                exchange_config['secret'] = self.config['secret']
                if 'passphrase' in self.config:
                    exchange_config['password'] = self.config['passphrase']
            
            self.exchange = exchange_class(exchange_config)
            logger.info(f"交易所连接成功: {self.exchange_name}")
        except Exception as e:
            logger.error(f"交易所连接失败: {str(e)}")
            raise
    
    def fetch_ohlcv(self, symbol: str, timeframe: str = '1m', limit: int = 100) -> List:
        """获取K线数据"""
        try:
            ohlcv = self.exchange.fetch_ohlcv(symbol, timeframe=timeframe, limit=limit)
            logger.debug(f"获取 {symbol} {timeframe} K线数据成功")
            return ohlcv
        except Exception as e:
            logger.error(f"获取K线数据失败 {symbol}: {str(e)}")
            return []
    
    def fetch_ticker(self, symbol: str) -> Optional[Dict]:
        """获取最新行情信息"""
        try:
            ticker = self.exchange.fetch_ticker(symbol)
            return ticker
        except Exception as e:
            logger.error(f"获取行情失败 {symbol}: {str(e)}")
            return None
    
    def fetch_balance(self) -> Optional[Dict]:
        """获取账户余额"""
        try:
            balance = self.exchange.fetch_balance()
            return balance
        except Exception as e:
            logger.error(f"获取余额失败: {str(e)}")
            return None
    
    def fetch_positions(self, symbol: str = None) -> List:
        """获取持仓信息"""
        try:
            if symbol:
                positions = self.exchange.fetch_positions([symbol])
            else:
                positions = self.exchange.fetch_positions()
            return positions if positions else []
        except Exception as e:
            logger.error(f"获取持仓失败: {str(e)}")
            return []
    
    def get_dataframe(self, symbol: str, timeframe: str = '1m', limit: int = 100) -> Optional[pd.DataFrame]:
        """获取K线数据并转换为DataFrame"""
        try:
            ohlcv = self.fetch_ohlcv(symbol, timeframe, limit)
            if not ohlcv:
                return None
            
            df = pd.DataFrame(
                ohlcv,
                columns=['timestamp', 'open', 'high', 'low', 'close', 'volume']
            )
            df['datetime'] = pd.to_datetime(df['timestamp'], unit='ms')
            df = df.set_index('datetime')
            
            return df
        except Exception as e:
            logger.error(f"转换DataFrame失败: {str(e)}")
            return None

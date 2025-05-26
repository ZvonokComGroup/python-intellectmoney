import datetime
import decimal
from enum import Enum, IntEnum, StrEnum
from typing import List, Optional, TypeAlias
from uuid import UUID

from pydantic import BaseModel, EmailStr


class Credentials(BaseModel):

    Login: str
    Password: str


class BearerData(BaseModel):

    token: str
    secret: str


class RequestState(IntEnum):

    Success = 0
    WithWarn = 1
    NoAuth = 2


class OperationState(BaseModel):

    Code: RequestState
    Desc: str


UserToken: TypeAlias = str


class UserTokenData(BaseModel):

    State: OperationState
    UserToken: UserToken


class InvoiceState(StrEnum):

    Created = 'Created'
    PartPaid = 'PartPaid'
    Paid = 'Paid'
    ToPaid = 'ToPaid'
    Refund = 'Refund'
    Held = 'Held'


class IsHoldingSearch(IntEnum):

    WithoutOrganizations = 0
    WithOrganizations = 1


class InvoiceSortOrder(str, Enum):

    CreationDate = 1
    ChangeDate = 2
    InvoiceState = 3
    Amount = 4


class GetInvoicesHistory(BaseModel):

    UserToken: UserToken
    EshopId: Optional[int] = None
    OrganizationId: Optional[int] = None
    State: Optional[InvoiceState] = None
    InvoiceId: Optional[int] = None
    IncludePaymentTransactions: Optional[bool] = None
    IsHoldingSearch: Optional[IsHoldingSearch] = None
    OwnerEmail: Optional[EmailStr] = None
    SortOrder: Optional[InvoiceSortOrder] = None
    DateFrom: Optional[datetime.date] = None
    DateTo: Optional[datetime.date] = None
    ChangeDateFrom: Optional[datetime.date] = None
    ChangeDateTo: Optional[datetime.date] = None
    Skip: Optional[int] = None
    Take: int


class OperationCode(int, Enum):

    Success = 0
    Process = 1
    Error = 2


class OperationState(BaseModel):

    Code: OperationCode
    Desc: str


class BaseResponse(BaseModel):

    OperationState: OperationState
    OperationId: Optional[UUID] = None
    EshopId: Optional[int] = None
    Result: Optional[dict] = None


class Currency(str, Enum):

    RUB = 'RUB'
    TST = 'TST'


class Money(BaseModel):

    Amount: decimal.Decimal
    Currency: Currency


class TransactionState(str, Enum):

    Created = 'Created'
    Confirm = 'Confirm'
    Canceled = 'Canceled'


class PaymentType(str, Enum):

    Entry = 'Entry'
    Purchase = 'Purchase'
    Refund = 'Refund'


class HistoryData(BaseModel):

    Id: int
    PaymentNumber: int
    State: TransactionState
    CreationDate: datetime.datetime
    PaymentAmount: Money
    RecipientAmount: Money
    PaymentAccount: str
    RecipientAccount: str
    Description: str
    InvoicePaymentType: PaymentType


class InvoiceData(BaseModel):

    Id: int
    State: InvoiceState
    CreationDate: datetime.datetime
    ChangeDate: datetime.datetime
    Amount: Money
    CurrentAmount: Money
    SurchargeAmount: Money
    Comment: str
    EShopId: int
    PurchaseOrderId: str
    HistoryList: Optional[List[HistoryData]] = None


class InvoicesHistoryList(BaseModel):

    State: OperationState
    InvoicesHistoryList: List[InvoiceData]


class InvoicesResponse(BaseResponse):

    Result: InvoicesHistoryList


class GetPaymentsHistory(BaseModel):

    UserToken: UserToken
    EshopId: Optional[int] = None
    PaymentTransactionId: Optional[int] = None
    DateFrom: Optional[datetime.date] = None
    DateTo: Optional[datetime.date] = None
    Skip: Optional[int] = None
    Take: int


class PaymentsHistoryList(BaseModel):

    State: OperationState
    InvoicesHistoryList: List[InvoiceData]


class PaymentsResponse(BaseResponse):

    Result: PaymentsHistoryList

from importlib.resources import Resource
from flaskblog import db
from flaskblog.models import OrganizationsUsersBelonging, Organizations, OrganizationsResourcesOwnership, Resources
from flaskblog.rooms.dtos import ResourceDto

class RoomsService:
    
    
    def search_available_rooms(user_id):
        '''
            与えられたuser_idのユーザーの所属するorganizationの所有するResourceのListを返す。
            何もなかった場合には空のListを返す。
            1. resourcesを所属するorganizationで絞り込み
            2. ResourceDtoを生成。
        '''


        rooms = Resources.query.join(
            OrganizationsResourcesOwnership, Resources.id==OrganizationsResourcesOwnership.resource_id)\
                .join(Organizations, OrganizationsResourcesOwnership.organization_id == Organizations.organization_id)\
                .join(OrganizationsUsersBelonging, Organizations.organization_id == OrganizationsUsersBelonging.organization_id)\
                .filter(OrganizationsUsersBelonging.user_id == user_id)\
                .all()

        return rooms

        orgs = db.session.query(OrganizationsUsersBelonging, Organizations).filter(OrganizationsUsersBelonging.organization_id == Organizations.organization_id)
        orgs = OrganizationsUsersBelonging.query.filter_by(user_id=user_id).join(Organizations, Organizations.id == OrganizationsUsersBelonging.organization_id)
        belongings = OrganizationsUsersBelonging.query.filter_by(user_id=user_id)
        organization_ids = [belonging.organization_id for belonging in belongings]
        organizations = Organizations.query.filter(Organizations.organization_id.in_(organization_ids))
        ownerships = OrganizationsResourcesOwnership.query.filter_by()

        #ownerships = OrganizationsResourcesOwnership.query.filter(OrganizationsResourcesOwnership.organization_id.in_(organization_ids))
        #resource_ids = [ownership.resource_id for ownership in ownerships]
        resources = Resources.query.filter(Resources.id.in_(resource_ids))

        '''
        部屋
        resources = Resources.query.filter(Resources.id.in_(resource_ids))
            resource.id
            resource.name
            resource.capacity
        ownership
            organization.name
        '''
       
        for org in organizations:
            for _  in org.organizations_resources_ownership:
                dbg = _
                